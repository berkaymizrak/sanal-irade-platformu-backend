# Generated by Django 4.1.7 on 2023-03-26 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GDPRConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('agreement', models.CharField(max_length=255, verbose_name='Agreement')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP address')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='Is accepted')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'GDPR Consent',
                'verbose_name_plural': 'GDPR Consents',
            },
        ),
    ]
