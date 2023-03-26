# Generated by Django 4.1.7 on 2023-03-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=10, verbose_name='Order')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL')),
                ('icon', models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('github', 'Github'), ('instagram', 'Instagram'), ('telegram', 'Telegram')], max_length=255, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social media',
                'verbose_name_plural': 'Social media links',
                'ordering': ('order',),
            },
        ),
    ]