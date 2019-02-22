# Generated by Django 2.0.7 on 2019-02-21 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('address_line_1', models.CharField(max_length=250)),
                ('address_line_2', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(default='United States of America', max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=250)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
            ],
        ),
        migrations.CreateModel(
            name='AddressPayementLivraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_payement_livraison_type', models.CharField(choices=[('facturation', 'Facturation'), ('LIVRAISON', 'Livraison')], max_length=120)),
                ('pays', models.CharField(default='Guinée', max_length=250)),
                ('ville', models.CharField(choices=[('conakry', 'Conakry'), ('boke', 'Boké'), ('boffa', 'Boffa'), ('fria', 'Fria'), ('gaoual', 'Gaoual'), ('koundara', 'Koundara'), ('dubreka', 'Dubreka'), ('kamsar', 'Kamsar'), ('kindia', 'Kindia'), ('forecariah', 'Forécariah'), ('coyah', 'Coyah'), ('telimele', 'Télimélé'), ('mamou', 'Mamou'), ('pita', 'Pita'), ('dalaba', 'Dalaba'), ('labe', 'Labé'), ('Lelouma', 'Lélouma'), ('mali', 'Mali yimbèrè'), ('koubia', 'Koubia'), ('tougue', 'Tougué'), ('faranah', 'Faranah'), ('dinguiraye', 'Dinguiraye'), ('kissidougou', 'Kissidougou'), ('dabola', 'Dabola'), ('kankan', 'Kankan'), ('siguiri', 'Siguiri'), ('madianah', 'Madianah'), ('kouroussa', 'Kouroussa'), ('nzerekore', "N'Zérékoré"), ('macenta', 'Macenta'), ('lola', 'Lola'), ('beyla', 'Beyla'), ('yomou', 'Yomou')], default='conakry', max_length=250)),
                ('quartier', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('mobile', models.CharField(max_length=250)),
                ('postal_code', models.CharField(blank=True, max_length=250, null=True)),
                ('payement_livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.PayementLivraison')),
            ],
        ),
    ]
