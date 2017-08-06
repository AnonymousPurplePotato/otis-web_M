# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-06 00:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(help_text='The Django Auth user attached to the student', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='assistant',
            field=models.ForeignKey(blank=True, help_text='The TA for this student, if any', null=True, on_delete=django.db.models.deletion.CASCADE, to='roster.TA'),
        ),
    ]