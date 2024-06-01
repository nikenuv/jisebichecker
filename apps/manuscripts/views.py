from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.db import transaction
from .forms import ManuscriptUploadForm
from django.contrib import messages
from django.contrib.auth.models import User
import magic
from . import checker
from .models import Manuscript, Report
from .forms import ManuscriptForm
from collections import OrderedDict
from xhtml2pdf import pisa
from io import BytesIO

def get_report(request, url):
    my_manuscript = Manuscript.objects.filter(manuscript_url=url).first()

    manuscript_id = my_manuscript.manuscript_id

    # Query the record with the specified field value
    my_report = Report.objects.filter(manuscript_id=manuscript_id).first()

    correct_count = 0
    for field in my_report._meta.fields[2:]:
        field_name = field.name
        field_value = getattr(my_report, field_name)

        if field_value == 1:
            correct_count += 1

    correct_percentage = int(round(correct_count/32*100, 0))
    wrong_percentage = int(round((32-correct_count)/32*100, 0))

    if my_report.title_size and my_report.title_bold:
        title_status = True
    else:
        title_status = False

    if my_report.author_size and my_report.author_bold:
        author_status = True
    else:
        author_status = False

    # if abs_background and abs_objectives and abs_methods and abs_result and abs_conclusion and abs_keywords and abs_sequential
    if all([my_report.abs_sequential, my_report.abs_background, my_report.abs_objectives, my_report.abs_methods, my_report.abs_result, my_report.abs_conclusion, my_report.abs_keywords]):
        abstract_status = True
    else:
        abstract_status = False

    if all([my_report.str_header_1_format, my_report.str_header_1_fsizetitle, my_report.str_header_1_fsizedetails, my_report.str_header_1_ffam, my_report.str_footer_1_format, my_report.str_footer_1_fsize, my_report.str_header_reg_format,my_report.str_header_reg_fsize, my_report. str_introduction, my_report.str_litrev, my_report.str_methods, my_report.str_result, my_report.str_discussion, my_report.str_conclusion, my_report.str_sequential]):
        structure_status = True
    else:
        structure_status = False

    additional_status = all([my_report.add_table, my_report.add_figure])

    reference_status = all([my_report.ref_format, my_report.ref_count, my_report.ref_used])

    report_data = {
        'file': url,
        'title': title_status,
        'author': author_status,
        'abstract': abstract_status,
        'structure': structure_status,
        'addition': additional_status,
        'reference': reference_status,
        'cek': my_report.title_size,
        'corrects': correct_count,
        'passed': correct_percentage,
        'failed': wrong_percentage,
        'manuscript': my_manuscript
    }

    return report_data

def report(request, url):
    
    report_data = get_report(request, url)
    # Set pesan flash untuk ditampilkan di halaman berikutnya
    return render(request, "manuscripts/report.html", context=report_data)


def full_report(request, url):

    my_manuscript = Manuscript.objects.filter(manuscript_url=url).first()

    manuscript_id = my_manuscript.manuscript_id

    # Query the record with the specified field value
    report = Report.objects.filter(manuscript_id=manuscript_id).first()

    report_data = {
        'file': my_manuscript.manuscript_url,
        'report': report,
    }

    return render(request, "manuscripts/full_report.html", context=report_data)


def history(request):
    # Mendapatkan parameter pengurutan dari URL, defaultnya adalah '-uploaded_at'

    sort_option = request.GET.get('sort', '-uploaded_at')

    # Validasi parameter pengurutan untuk mencegah serangan injeksi
    valid_sort_options = ['uploaded_at', '-uploaded_at',
                          'manuscript_title', '-manuscript_title']
    if sort_option not in valid_sort_options:
        sort_option = '-uploaded_at'  # Default jika parameter tidak valid

    # Mengambil semua data manuscript milik user dan mengurutkannya berdasarkan sort_option
    manuscripts = Manuscript.objects.filter(
        user=request.user).order_by(sort_option)

    context = {'manuscripts': manuscripts, 'current_sort': sort_option,}
    return render(request, "manuscripts/history.html", context)


def download(request, url):

    report_data = get_report(request, url)

    my_manuscript = Manuscript.objects.filter(manuscript_url=url).first()

    manuscript_id = my_manuscript.manuscript_id

    # Query the record with the specified field value
    full_report = Report.objects.filter(manuscript_id=manuscript_id).first()

    report_data.update({'report': full_report})
    print(report_data)

    template = get_template("manuscripts/download.html")
    html = template.render(context=report_data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)

    return HttpResponse(result.getvalue(),content_type="application/pdf")
    return None

def upload(request):
    if request.method == 'POST':
        form = ManuscriptUploadForm(request.POST, request.FILES)
        manuscript_file = request.FILES["manuscript_file"]
        mime = magic.Magic(mime=True)
        filetype = mime.from_buffer(manuscript_file.read())
        if filetype == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":

            filename = User.objects.make_random_password(10)

            new_manuscript = Manuscript(manuscript_title=checker.get_title(manuscript_file),
                                        manuscript_authors=checker.get_author(
                                            manuscript_file),
                                        manuscript_url=filename+".docx",
                                        user=request.user)
            
            with open('media/' + filename+".docx", 'wb+') as destination:
                for chunk in manuscript_file.chunks():
                    destination.write(chunk)

            directory = "media/" + filename + ".docx"

            new_report = Report(manuscript=new_manuscript,
                                title_size=checker.cek_title(directory)[0],
                                title_bold=checker.cek_title(directory)[1],
                                author_size=checker.cek_author(directory)[0],
                                author_bold=checker.cek_author(directory)[1],
                                abs_background=checker.cek_abstrak_sequential(directory)[0],
                                abs_objectives=checker.cek_abstrak_sequential(directory)[1],
                                abs_methods=checker.cek_abstrak_sequential(directory)[2],
                                abs_result=checker.cek_abstrak_sequential(directory)[3],
                                abs_conclusion=checker.cek_abstrak_sequential(directory)[4],
                                abs_keywords=checker.cek_abstrak_sequential(directory)[5],
                                abs_sequential=checker.cek_abstrak_sequential(directory)[6],
                                abs_keywords_count=checker.cek_abstrak_sequential(directory)[7],
                                abs_words_count=checker.cek_abstrak_sequential(directory)[8],
                                str_header_1_format=checker.cek_header_1(directory)["format"],
                                str_header_1_fsizetitle=checker.cek_header_1(directory)["font_size_title"],
                                str_header_1_fsizedetails=checker.cek_header_1(directory)["font_size_details"],
                                str_header_1_ffam=checker.cek_header_1(directory)["font_family"],
                                str_footer_1_format=checker.cek_footer(directory)['format'],
                                str_footer_1_fsize=checker.cek_footer(directory)['font_size'],
                                str_header_reg_format=checker.cek_header_normal(directory)["format"],
                                str_header_reg_fsize=checker.cek_header_normal(directory)["font_size"],
                                str_introduction=checker.cek_struktur(directory)['introduction'],
                                str_litrev=checker.cek_litrev(directory),
                                str_methods=checker.cek_struktur(directory)["method"],
                                str_result=checker.cek_struktur(directory)["result"],
                                str_discussion=checker.cek_struktur(directory)["discussion"],
                                str_conclusion=checker.cek_struktur(directory)["conclusion"],
                                str_sequential=checker.cek_struktur(directory)["sort"],
                                add_table=checker.cek_tabel(directory),
                                add_figure=checker.cek_figure(directory),
                                ref_format=checker.cek_reference(directory)["format"],
                                ref_count=checker.cek_reference(directory)["count"],
                                ref_used=checker.cek_reference(directory)["used"]
                                )
            
            with transaction.atomic():
                new_manuscript.save()
                new_report.save()

            return redirect('report', url=new_manuscript.manuscript_url)
        else:
            return render(request, 'manuscripts/upload.html')
    return render(request, 'manuscripts/upload.html')


def search_history(request):
    if request.method == 'POST':
        search_query = request.POST["search"]
        if search_query == "":
            return history(request)

        results = Manuscript.objects.filter(
            manuscript_title__icontains=search_query)
        return render(request, 'manuscripts/history.html', {'search': search_query, 'search_result': results})


# def search_history(request):
#     if request.method == 'POST':
#         search_query = request.POST.get("search", "")
#         if search_query == "":
#             return history(request)

#         # Mendapatkan parameter pengurutan dari URL, defaultnya adalah '-uploaded_at'
#         sort_option = request.GET.get('sort', '-uploaded_at')

#         # Validasi parameter pengurutan untuk mencegah serangan injeksi
#         valid_sort_options = ['uploaded_at', '-uploaded_at',
#                               'manuscript_title', '-manuscript_title']
#         if sort_option not in valid_sort_options:
#             sort_option = '-uploaded_at'  # Default jika parameter tidak valid

#         results = Manuscript.objects.filter(
#             manuscript_title__icontains=search_query, user=request.user
#         ).order_by(sort_option)

#         context = {'search': search_query,
#                    'search_result': results, 'current_sort': sort_option}
#         return render(request, 'manuscripts/history.html', context)
