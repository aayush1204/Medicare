# Generated by Django 2.2.4 on 2019-10-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_tempdoctormodel_temppatientmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempdoctormodel',
            name='did',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='temppatientmodel',
            name='pid',
            field=models.IntegerField(max_length=4),
        ),
    ]
