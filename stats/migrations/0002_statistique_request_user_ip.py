# Generated by Django 2.0.7 on 2018-09-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistique',
            name='request_user_ip',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]