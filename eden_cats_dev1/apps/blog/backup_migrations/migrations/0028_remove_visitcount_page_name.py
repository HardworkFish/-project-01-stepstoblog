# Generated by Django 2.0.5 on 2018-08-31 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20180827_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitcount',
            name='page_name',
        ),
    ]