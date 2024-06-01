from django.db import models
from django.contrib.auth.models import User

class Manuscript(models.Model):
    manuscript_id = models.AutoField(db_column='MANUSCRIPT_ID', primary_key=True)  # Field name made lowercase.
    manuscript_title = models.TextField(db_column='MANUSCRIPT_TITLE')  # Field name made lowercase.
    manuscript_authors = models.CharField(db_column='MANUSCRIPT_AUTHORS', max_length=255)  # Field name made lowercase.
    manuscript_url = models.TextField(db_column='MANUSCRIPT_URL')  # Field name made lowercase.
    uploaded_at = models.DateTimeField(db_column='UPLOADED_AT', auto_now_add=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'manuscript'


class Report(models.Model):
    report_id = models.AutoField(db_column='REPORT_ID', primary_key=True)  # Field name made lowercase.
    manuscript = models.ForeignKey(Manuscript, models.DO_NOTHING, db_column='MANUSCRIPT_ID')  # Field name made lowercase.
    title_size = models.IntegerField(db_column='TITLE_SIZE', blank=True, null=True)  # Field name made lowercase.
    title_bold = models.IntegerField(db_column='TITLE_BOLD', blank=True, null=True)  # Field name made lowercase.
    author_size = models.IntegerField(db_column='AUTHOR_SIZE', blank=True, null=True)  # Field name made lowercase.
    author_bold = models.IntegerField(db_column='AUTHOR_BOLD', blank=True, null=True)  # Field name made lowercase.
    abs_background = models.IntegerField(db_column='ABS_BACKGROUND', blank=True, null=True)  # Field name made lowercase.
    abs_objectives = models.IntegerField(db_column='ABS_OBJECTIVES', blank=True, null=True)  # Field name made lowercase.
    abs_methods = models.IntegerField(db_column='ABS_METHODS', blank=True, null=True)  # Field name made lowercase.
    abs_result = models.IntegerField(db_column='ABS_RESULT', blank=True, null=True)  # Field name made lowercase.
    abs_conclusion = models.IntegerField(db_column='ABS_CONCLUSION', blank=True, null=True)  # Field name made lowercase.
    abs_keywords = models.IntegerField(db_column='ABS_KEYWORDS', blank=True, null=True)
    abs_keywords_count = models.IntegerField(db_column='ABS_KEYWORDS_COUNT', blank=True, null=True)  # Field name made lowercase.
    abs_words_count = models.IntegerField(db_column='ABS_WORDS_COUNT', blank=True, null=True)  # Field name made lowercase.
    abs_sequential = models.IntegerField(db_column='ABS_SEQUENTIAL', blank=True, null=True)  # Field name made lowercase.
    str_header_1_format = models.IntegerField(db_column='STR_HEADER_1_FORMAT', blank=True, null=True)  # Field name made lowercase.
    str_header_1_fsizetitle = models.IntegerField(db_column='STR_HEADER_1_FSIZETITLE', blank=True, null=True)  # Field name made lowercase.
    str_header_1_fsizedetails = models.IntegerField(db_column='STR_HEADER_1_FSIZEDETAILS', blank=True, null=True)  # Field name made lowercase.
    str_header_1_ffam = models.IntegerField(db_column='STR_HEADER_1_FFAM', blank=True, null=True)  # Field name made lowercase.
    str_footer_1_format = models.IntegerField(db_column='STR_FOOTER_1_FORMAT', blank=True, null=True)  # Field name made lowercase.
    str_footer_1_fsize = models.IntegerField(db_column='STR_FOOTER_1_FSIZE', blank=True, null=True)  # Field name made lowercase.
    str_header_reg_format = models.IntegerField(db_column='STR_HEADER_REG_FORMAT', blank=True, null=True)  # Field name made lowercase.
    str_header_reg_fsize = models.IntegerField(db_column='STR_HEADER_REG_FSIZE', blank=True, null=True)  # Field name made lowercase.
    str_introduction = models.IntegerField(db_column='STR_INTRODUCTION', blank=True, null=True)  # Field name made lowercase.
    str_litrev = models.IntegerField(db_column='STR_LITREV', blank=True, null=True)  # Field name made lowercase.
    str_methods = models.IntegerField(db_column='STR_METHODS', blank=True, null=True)  # Field name made lowercase.
    str_result = models.IntegerField(db_column='STR_RESULT', blank=True, null=True)  # Field name made lowercase.
    str_discussion = models.IntegerField(db_column='STR_DISCUSSION', blank=True, null=True)  # Field name made lowercase.
    str_conclusion = models.IntegerField(db_column='STR_CONCLUSION', blank=True, null=True)  # Field name made lowercase.
    str_sequential = models.IntegerField(db_column='STR_SEQUENTIAL', blank=True, null=True)  # Field name made lowercase.
    add_table = models.IntegerField(db_column='ADD_TABLE', blank=True, null=True)  # Field name made lowercase.
    add_figure = models.IntegerField(db_column='ADD_FIGURE', blank=True, null=True)  # Field name made lowercase.
    ref_format = models.IntegerField(db_column='REF_FORMAT', blank=True, null=True)  # Field name made lowercase.
    ref_count = models.IntegerField(db_column='REF_COUNT', blank=True, null=True)  # Field name made lowercase.
    ref_used = models.IntegerField(db_column='REF_USED', blank=True, null=True)  # Field name made lowercase.
 
    class Meta:
        managed = True
        db_table = 'report'
