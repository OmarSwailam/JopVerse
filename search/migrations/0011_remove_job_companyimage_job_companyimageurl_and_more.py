# Generated by Django 4.1.4 on 2022-12-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_alter_job_joburl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='companyImage',
        ),
        migrations.AddField(
            model_name='job',
            name='companyImageUrl',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='websiteIcon',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
