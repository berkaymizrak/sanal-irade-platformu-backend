# Generated by Django 4.1.7 on 2023-03-26 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0002_alter_socialmedia_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BallotBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('box_number', models.PositiveIntegerField(default=0, verbose_name='Box Number')),
                ('district', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.district', verbose_name='District')),
            ],
            options={
                'verbose_name': 'Ballot Box',
                'verbose_name_plural': 'Ballot Boxes',
                'ordering': ('-election__start_date', 'box_number'),
            },
        ),
        migrations.CreateModel(
            name='BallotBoxReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('report', models.FileField(blank=True, default='', upload_to='elections/reports/', verbose_name='Report')),
                ('total_votes', models.PositiveIntegerField(default=0, verbose_name='Total Votes')),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('ballot_box', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.ballotbox', verbose_name='Ballot Box')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Ballot Box Report',
                'verbose_name_plural': 'Ballot Box Reports',
                'ordering': ('-ballot_box__election__start_date', '-created_date'),
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('start_date', models.DateTimeField(auto_now=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(auto_now=True, verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Election',
                'verbose_name_plural': 'Elections',
                'ordering': ('translations__name',),
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='ElectionCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('logo', models.ImageField(blank=True, default='', upload_to='elections/candidates/', verbose_name='Logo')),
                ('election', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.election', verbose_name='Election')),
            ],
            options={
                'verbose_name': 'Election Candidate',
                'verbose_name_plural': 'Election Candidates',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ElectionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('votes', models.PositiveIntegerField(default=0, verbose_name='Votes')),
                ('ballot_box', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.ballotbox', verbose_name='Ballot Box')),
                ('candidate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.electioncandidate', verbose_name='Election Candidate')),
            ],
            options={
                'verbose_name': 'Election Result',
                'verbose_name_plural': 'Election Results',
                'ordering': ('votes',),
            },
        ),
        migrations.CreateModel(
            name='CandidateReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('votes', models.PositiveIntegerField(default=0, verbose_name='Votes')),
                ('ballet_box_report', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.ballotboxreport', verbose_name='Ballot Box Report')),
                ('candidate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.electioncandidate', verbose_name='Election Candidate')),
            ],
            options={
                'verbose_name': 'Candidate Report',
                'verbose_name_plural': 'Candidate Reports',
                'ordering': ('-ballet_box_report', '-created_date'),
            },
        ),
        migrations.AddField(
            model_name='ballotbox',
            name='election',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.election', verbose_name='Election'),
        ),
        migrations.CreateModel(
            name='ElectionTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='election.election')),
            ],
            options={
                'verbose_name': 'Election Translation',
                'db_table': 'election_election_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
