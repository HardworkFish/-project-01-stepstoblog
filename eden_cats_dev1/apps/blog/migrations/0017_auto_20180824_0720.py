# Generated by Django 2.0.5 on 2018-08-23 23:20

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180824_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='digest',
            field=mdeditor.fields.MDTextField(blank=True, max_length=500, verbose_name='文章摘要'),
        ),
    ]
