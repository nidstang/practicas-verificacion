# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(verbose_name=b'date plublished')),
                ('content', models.CharField(max_length=1024)),
                ('author', models.ForeignKey(to='users.User')),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
