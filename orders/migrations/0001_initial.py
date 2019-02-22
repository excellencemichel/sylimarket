# Generated by Django 2.0.7 on 2019-02-21 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('addresses', '0001_initial'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], default='created', max_length=250)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_pdf', models.FileField(blank=True, null=True, upload_to='pdfs')),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='addresses.Address')),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='addresses.Address')),
            ],
            options={
                'verbose_name': 'Commande avec payement à la carte bancaire',
                'verbose_name_plural': 'Commandes avec payements à la carte bancaire',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
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
                'verbose_name': 'Commande avec payement à la livraison',
                'verbose_name_plural': 'Commandes de payements à la livraison',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='ProductPurshase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=120)),
                ('refunded', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.CartItem')),
            ],
            options={
                'verbose_name': 'Produit payé avec payement par carte bancaire',
                'verbose_name_plural': 'Produits payés avec payements par carte bancaire',
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
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.CartItem')),
                ('payement_livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.PayementLivraison')),
            ],
            options={
                'verbose_name': 'Produit payé à la livraison',
                'verbose_name_plural': 'Produits payés à la livraison',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
