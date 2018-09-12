# Generated by Django 2.0.7 on 2018-09-07 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_payementlivraison'),
        ('addresses', '0002_addresspayementlivraison'),
        ('carts', '0002_auto_20180830_1730'),
        ('products', '0019_auto_20180901_0239'),
        ('orders', '0014_order_order_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPayementLivraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_payement_livraison_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], default='created', max_length=250)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_payement_livraison_pdf', models.FileField(blank=True, null=True, upload_to='order_p_l_pdfs')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('facturation_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facturation_address', to='addresses.AddressPayementLivraison')),
                ('livraison_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livraison_address', to='addresses.AddressPayementLivraison')),
                ('payement_livraison', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.PayementLivraison')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='ProductPurshasePayementLivraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_payement_livraison_id', models.CharField(max_length=120)),
                ('refunded', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('payement_livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.PayementLivraison')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
