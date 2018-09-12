# Generated by Django 2.0.7 on 2018-09-01 01:37

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20180830_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/michel/galilee/static_cdn/protected_root'), upload_to=products.models.upload_product_file_loc),
        ),
    ]
