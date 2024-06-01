# forms.py
from django import forms
from .models import Manuscript, Report

class ManuscriptUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    uploaded_file = forms.FileField()

class ManuscriptForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Manuscript
        fields = "__all__"

class ReportForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Report
        fields = "__all__"