# Generated by Django 2.0.5 on 2018-09-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('hide', '隐藏'), ('public', '公开'), ('delete', '删除')], default='public', max_length=10, verbose_name='留言状态'),
        ),
    ]