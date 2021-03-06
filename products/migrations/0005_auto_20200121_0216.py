# Generated by Django 2.0.7 on 2020-01-21 01:16

from django.db import migrations, models
import django.db.models.deletion
import utils.files_utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191223_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beauty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
                ('promotion', models.DecimalField(blank=True, decimal_places=2, max_digits=40, null=True)),
                ('taux_taxe', models.PositiveIntegerField(default=0)),
                ('taxe', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('stock', models.PositiveIntegerField()),
                ('featured', models.BooleanField(default=False)),
                ('special', models.BooleanField(default=False)),
                ('solde', models.BooleanField(default=False)),
                ('pourcentage', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('image', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('marque', models.CharField(max_length=250)),
                ('product_model', models.CharField(max_length=250)),
                ('beauty_type', models.CharField(choices=[('parfum', 'Le parfum'), ('savon', 'Le savon'), ('gel', 'Le gel'), ('shampoing', 'Savon shampoing'), ('huile', 'Huile crème'), ('vitamine', 'Vitamine'), ('soins', 'Produits de soins')], max_length=250)),
            ],
            options={
                'verbose_name': 'Produit de beauté',
                'verbose_name_plural': 'Produits de beauté',
            },
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
                ('promotion', models.DecimalField(blank=True, decimal_places=2, max_digits=40, null=True)),
                ('taux_taxe', models.PositiveIntegerField(default=0)),
                ('taxe', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('stock', models.PositiveIntegerField()),
                ('featured', models.BooleanField(default=False)),
                ('special', models.BooleanField(default=False)),
                ('solde', models.BooleanField(default=False)),
                ('pourcentage', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('image', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('marque', models.CharField(max_length=250)),
                ('product_model', models.CharField(max_length=250)),
                ('health_type', models.CharField(choices=[('aliment', 'Aliment'), ('vitamine', 'Vitamine'), ('soins', 'Pour les soins'), ('pharmaeutique', 'Phamaceutique'), ('parapharmaeutique', 'Paraphamaceutique')], max_length=250)),
            ],
            options={
                'verbose_name': 'Produit de santé',
                'verbose_name_plural': 'Produits de santé',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('men_clothing', 'Vetements'), ('women_clothing', 'Vetements'), ('men_clothing', 'Vetements'), ('clothing_accessoire', 'Accessoires de Vetements'), ('pantalon', 'Pantalon'), ('culotte', 'Culotte'), ('jupe', 'Jupe'), ('men_shoe', 'Chaussure pour homme'), ('women_shoe', 'Chaussure pour femme '), ('phone', 'Phone'), ('tablette', 'Tablette'), ('phone_accessoire', 'Accessoire de phone'), ('computer', 'Ordinateur'), ('computer_accessoire', 'Accessoire pour Ordinateur'), ('watch', 'Montre'), ('audio_viduel', 'Audio Visuel'), ('electromenager', 'Électromenager'), ('beauty', 'Beauté'), ('health', 'Health')], max_length=250),
        ),
        migrations.AddField(
            model_name='health',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health', to='products.Product'),
        ),
        migrations.AddField(
            model_name='beauty',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beauty', to='products.Product'),
        ),
    ]
