# Generated by Django 4.1.4 on 2022-12-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_alter_job_joburl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobUrl',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
