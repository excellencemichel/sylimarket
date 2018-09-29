# Generated by Django 2.0.7 on 2018-09-29 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_statistique_request_user_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistique',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistique',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]