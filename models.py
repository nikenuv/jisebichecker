# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Manuscript(models.Model):
    manuscript_id = models.AutoField(db_column='MANUSCRIPT_ID', primary_key=True)  # Field name made lowercase.
    manuscript_title = models.TextField(db_column='MANUSCRIPT_TITLE')  # Field name made lowercase.
    manuscript_authors = models.CharField(db_column='MANUSCRIPT_AUTHORS', max_length=255)  # Field name made lowercase.
    manuscript_url = models.TextField(db_column='MANUSCRIPT_URL')  # Field name made lowercase.
    uploaded_at = models.DateTimeField(db_column='UPLOADED_AT')  # Field name made lowercase.
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manuscript'


class Report(models.Model):
    report_id = models.AutoField(db_column='REPORT_ID', primary_key=True)  # Field name made lowercase.
    manuscript = models.ForeignKey(Manuscript, models.DO_NOTHING, db_column='MANUSCRIPT_ID')  # Field name made lowercase.
    title_size = models.IntegerField(db_column='TITLE_SIZE')  # Field name made lowercase.
    title_bold = models.IntegerField(db_column='TITLE_BOLD')  # Field name made lowercase.
    author_size = models.IntegerField(db_column='AUTHOR_SIZE')  # Field name made lowercase.
    author_bold = models.IntegerField(db_column='AUTHOR_BOLD')  # Field name made lowercase.
    abs_background = models.IntegerField(db_column='ABS_BACKGROUND')  # Field name made lowercase.
    abs_objectives = models.IntegerField(db_column='ABS_OBJECTIVES')  # Field name made lowercase.
    abs_methods = models.IntegerField(db_column='ABS_METHODS')  # Field name made lowercase.
    abs_result = models.IntegerField(db_column='ABS_RESULT')  # Field name made lowercase.
    abs_conclusion = models.IntegerField(db_column='ABS_CONCLUSION')  # Field name made lowercase.
    abs_keywords = models.IntegerField(db_column='ABS_KEYWORDS')  # Field name made lowercase.
    abs_sequential = models.IntegerField(db_column='ABS_SEQUENTIAL')  # Field name made lowercase.
    str_header_1 = models.IntegerField(db_column='STR_HEADER_1')  # Field name made lowercase.
    str_footer_1 = models.IntegerField(db_column='STR_FOOTER_1')  # Field name made lowercase.
    str_header_reg = models.IntegerField(db_column='STR_HEADER_REG')  # Field name made lowercase.
    str_introduction = models.IntegerField(db_column='STR_INTRODUCTION')  # Field name made lowercase.
    str_litrev = models.IntegerField(db_column='STR_LITREV')  # Field name made lowercase.
    str_methods = models.IntegerField(db_column='STR_METHODS')  # Field name made lowercase.
    str_result = models.IntegerField(db_column='STR_RESULT')  # Field name made lowercase.
    str_discussion = models.IntegerField(db_column='STR_DISCUSSION')  # Field name made lowercase.
    str_conclusion = models.IntegerField(db_column='STR_CONCLUSION')  # Field name made lowercase.
    str_sequential = models.IntegerField(db_column='STR_SEQUENTIAL')  # Field name made lowercase.
    add_table = models.IntegerField(db_column='ADD_TABLE')  # Field name made lowercase.
    add_figure = models.IntegerField(db_column='ADD_FIGURE')  # Field name made lowercase.
    add_equation = models.IntegerField(db_column='ADD_EQUATION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'report'
