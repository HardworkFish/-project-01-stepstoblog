# Generated by Django 2.0.5 on 2018-08-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180818_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', '草稿'), ('publish', '发表')], default='publish', max_length=10, verbose_name='文章状态'),
        ),
    ]