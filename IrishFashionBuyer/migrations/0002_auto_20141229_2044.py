# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('IrishFashionBuyer', '0001_initial')]

    operations = [
        migrations.AddField(
            field = models.CharField(default='No Comments', max_length=2000, blank=True),
            name = 'order_comments',
            model_name = 'order',
        ),
        migrations.AlterField(
            field = models.CharField(default='Not available', max_length=500),
            name = 'delivery_number',
            model_name = 'order',
        ),
    ]
