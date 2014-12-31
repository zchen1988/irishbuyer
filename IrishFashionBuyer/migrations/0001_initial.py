# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.CharField(max_length=500)),
                ('order_time', models.DateTimeField()),
                ('total_price', models.CharField(default=b'0', max_length=200)),
                ('delivery_address', models.CharField(default=b'Test', max_length=500)),
                ('delivery_number', models.CharField(default=b'Not available', max_length=500)),
                ('order_paid', models.BooleanField()),
                ('order_comments', models.CharField(default=b'No Comments', max_length=2000, blank=True)),
                ('order_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.CharField(max_length=500)),
                ('product_name', models.CharField(max_length=200)),
                ('order_time', models.DateTimeField()),
                ('product_price', models.FloatField()),
                ('product_quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
