# Generated by Django 4.2.3 on 2023-12-31 02:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('websites', '0002_alter_website_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('http_status', models.CharField(choices=[('100', 'Continue'), ('101', 'Switching protocols'), ('102', 'Processing'), ('103', 'Early Hints'), ('200', 'OK'), ('201', 'Created'), ('202', 'Accepted'), ('203', 'Non-Authoritative Information'), ('204', 'No Content'), ('205', 'Reset Content'), ('206', 'Partial Content'), ('207', 'Multi-Status'), ('208', 'Already Reported'), ('226', 'IM Used'), ('300', 'Multiple Choices'), ('301', 'Moved Permanently'), ('302', 'Found (Previously "Moved Temporarily")'), ('303', 'See Other'), ('304', 'Not Modified'), ('305', 'Use Proxy'), ('306', 'Switch Proxy'), ('307', 'Temporary Redirect'), ('308', 'Permanent Redirect'), ('400', 'Bad Request'), ('401', 'Unauthorized'), ('402', 'Payment Required'), ('403', 'Forbidden'), ('404', 'Not Found'), ('405', 'Method Not Allowed'), ('406', 'Not Acceptable'), ('407', 'Proxy Authentication Required'), ('408', 'Request Timeout'), ('409', 'Conflict'), ('410', 'Gone'), ('411', 'Length Required'), ('412', 'Precondition Failed'), ('413', 'Payload Too Large'), ('414', 'URI Too Long'), ('415', 'Unsupported Media Type'), ('416', 'Range Not Satisfiable'), ('417', 'Expectation Failed'), ('418', 'Im a Teapot'), ('421', 'Misdirected Request'), ('422', 'Unprocessable Entity'), ('423', 'Locked'), ('424', 'Failed Dependency'), ('425', 'Too Early'), ('426', 'Upgrade Required'), ('428', 'Precondition Required'), ('429', 'Too Many Requests'), ('431', 'Request Header Fields Too Large'), ('451', 'Unavailable For Legal Reasons'), ('500', 'Internal Server Error'), ('501', 'Not Implemented'), ('502', 'Bad Gateway'), ('503', 'Service Unavailable'), ('504', 'Gateway Timeout'), ('505', 'HTTP Version Not Supported'), ('506', 'Variant Also Negotiates'), ('507', 'Insufficient Storage'), ('508', 'Loop Detected'), ('510', 'Not Extended'), ('511', 'Network Authentication Required')], default=('200', 'OK'), verbose_name='Http Status Code')),
                ('status', models.CharField(choices=[('CHECKING', 'Checking website'), ('REMOVED', 'Removed website'), ('CHECKED', 'Checked website'), ('BACKUPED', 'Backuped website'), ('TRANSFERED', 'Transfered Website'), ('POSTPONED', 'Hold over/Postponed')], default=(('CHECKING', 'Checking website'),), verbose_name='Status')),
                ('request_of', models.CharField(choices=[('REQUEST_REMOVE', 'Remove website'), ('REQUEST_CHECK', 'Check website'), ('REQUEST_BACKUP', 'Backup website'), ('REQUEST_CHECK_SSL', 'Check SSL Status'), ('REQUEST_TRANSFER_TO_SERVER', 'Transfer to another server (inside our systems)'), ('REQUEST_TRANSFER_TO_CLIENT_PROVIDER', 'Transfer to another clients provider')], default=('REQUEST_CHECK', 'Check website'), verbose_name='Request of')),
                ('incident_date', models.DateTimeField(auto_now_add=True, verbose_name='incident date')),
                ('description', models.TextField(max_length=700, verbose_name='Description')),
                ('action', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/incidents')),
                ('from_website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.website', verbose_name='Website')),
            ],
            options={
                'verbose_name': 'report',
                'verbose_name_plural': 'reports',
                'ordering': ['incident_date'],
            },
        ),
    ]