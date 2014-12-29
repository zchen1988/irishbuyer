# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [(u'auth', '__first__')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('order_number', models.CharField(max_length=500),), ('product_name', models.CharField(max_length=200),), ('order_time', models.DateTimeField(),), ('product_price', models.FloatField(),), ('product_quantity', models.IntegerField(),)],
            bases = (models.Model,),
            options = {},
            name = 'OrderDetails',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('order_number', models.CharField(max_length=500),), ('order_time', models.DateTimeField(),), ('total_price', models.CharField(default='0', max_length=200),), ('delivery_address', models.CharField(default='Test', max_length=500),), ('delivery_number', models.CharField(default='111', max_length=500),), ('order_paid', models.BooleanField(),), ('order_user', models.ForeignKey(to=u'auth.User', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'Order',
        ),
    ]
