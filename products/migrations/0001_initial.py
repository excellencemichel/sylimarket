# Generated by Django 2.0.7 on 2019-04-17 22:49

from django.db import migrations, models
import django.db.models.deletion
import utils.files_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoireClothng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('accessoire_type', models.CharField(choices=[('ceinture', 'Ceinteure'), ('lunette', 'Lunette'), ('kepi', 'Képi'), ('foular', 'Foular'), ('chausette', 'Chaussette'), ('cravate', 'Cravate'), ('echarpe', 'Echarpe')], max_length=250)),
                ('genre', models.CharField(choices=[('hommes', 'Pour homme'), ('femmes', 'Pour homme'), ('mix', 'Pour tous le monde')], default='mix', max_length=250)),
                ('caracteristque', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessoireComputer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('accesoire_computer', models.CharField(choices=[('disquedur', 'Disque dur'), ('chargeur', 'Chargeur'), ('micro', 'Micro'), ('logiciel', 'Logiciel'), ('clavier', 'Clavier'), ('ecran', 'Ecran')], max_length=250)),
                ('caracteristque', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessoirePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('accessoire_type', models.CharField(choices=[('ecouteurs', 'Ecouteurs'), ('chargeur', 'Chargeur'), ('pochette', 'Pochette'), ('anticasse', 'Anti casse'), ('ecran', 'Ecran'), ('batterie', 'Batterie')], max_length=250)),
                ('caracteristique', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('computer_type', models.CharField(choices=[('pc', 'Ordinateur portable'), ('bureatique', 'Ordinateur bureatique')], default='pc', max_length=250)),
                ('computer_model', models.CharField(max_length=250)),
                ('image_ouvert', models.FileField(max_length=250, upload_to=utils.files_utils.upload_file_location)),
                ('image_dos', models.FileField(max_length=250, upload_to=utils.files_utils.upload_file_location)),
                ('image_haut', models.FileField(max_length=250, upload_to=utils.files_utils.upload_file_location)),
                ('image_bas', models.FileField(max_length=250, upload_to=utils.files_utils.upload_file_location)),
                ('image_gauche', models.FileField(max_length=250, upload_to=utils.files_utils.upload_file_location)),
                ('image_droite', models.FileField(max_length=250, upload_to=utils.files_utils.upload_file_location)),
                ('disque_dur', models.CharField(max_length=250)),
                ('processeur', models.CharField(max_length=250)),
                ('memoire_ram', models.CharField(max_length=100)),
                ('affichage', models.CharField(max_length=250)),
                ('systeme_exploitation', models.CharField(max_length=250)),
                ('connectivite', models.CharField(max_length=250)),
                ('ports', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Culotte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('image_derriere', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_devant', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('genre', models.CharField(choices=[('hommes', 'Hommes'), ('femmes', 'Femmes'), ('mix', 'Mix')], max_length=250)),
                ('tranche', models.CharField(choices=[('allage', 'Pour tous les âges'), ('moins40', 'Moins de 40 ans'), ('moins20', 'Moins de 20 ans'), ('plus40', 'Plus de 40 ans'), ('moins12', 'Moins de 12 ans')], max_length=250)),
                ('numero', models.CharField(max_length=250)),
                ('culotte_type', models.CharField(choices=[('jeans', 'Culotte Jeans'), ('jggin', 'Culotte Jogging'), ('chino', 'Culotte Chino'), ('tissu', 'Culotte Tissu '), ('nilon', 'Culotte en nilon')], max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('image_derriere', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_devant', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('tranche', models.CharField(choices=[('allage', 'Pour tous les âges'), ('moins40', 'Moins de 40 ans'), ('moins20', 'Moins de 20 ans'), ('plus40', 'Plus de 40 ans'), ('moins12', 'Moins de 12 ans')], max_length=250)),
                ('taille', models.CharField(choices=[('moyenne', 'Taille moyenne'), ('courte', 'Taille courte'), ('longue', 'Taille longue')], max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenClothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('image_derriere', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_devant', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('taille', models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=250)),
                ('genre', models.CharField(choices=[('hommes', 'Hommes'), ('femmes', 'Femmes'), ('mix', 'Mix')], max_length=250)),
                ('manche', models.CharField(choices=[('courte', 'Courte'), ('longue', 'Longue')], max_length=250)),
                ('tranche', models.CharField(choices=[('allage', 'Pour tous les âges'), ('moins40', 'Moins de 40 ans'), ('moins20', 'Moins de 20 ans'), ('plus40', 'Plus de 40 ans'), ('moins12', 'Moins de 12 ans')], max_length=250)),
                ('clothing_type', models.CharField(choices=[('shirt', 'Chemise'), ('tshirt', 'T-Shirt'), ('jacket', 'Jacket'), ('bluson', 'Bluson'), ('pull', 'Pulls'), ('polo', 'Polo'), ('maillot', 'Maillot'), ('gilet', 'Gilet')], max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenShoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('genre', models.CharField(choices=[('hommes', 'Hommes'), ('femmes', 'Femmes'), ('mix', 'Mix')], max_length=250)),
                ('tranche', models.CharField(choices=[('allage', 'Pour tous les âges'), ('moins40', 'Moins de 40 ans'), ('moins20', 'Moins de 20 ans'), ('plus40', 'Plus de 40 ans'), ('moins12', 'Moins de 12 ans')], max_length=250)),
                ('image_haut', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_dos', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_gauche', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_droite', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_derriere', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_devant', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('numero', models.CharField(max_length=250)),
                ('shoes_type', models.CharField(choices=[('basket', 'Basket'), ('reposepied', 'Repose pied'), ('soulier', 'Soulier'), ('sandale', 'Sandale'), ('tenis', 'Tenis'), ('mocassin', 'Mocassin'), ('espadrille', 'Espadrille'), ('running', 'Running'), ('max', 'Chaussure max grande taille')], max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pantalon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('image_derriere', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_devant', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('genre', models.CharField(choices=[('hommes', 'Hommes'), ('femmes', 'Femmes'), ('mix', 'Mix')], max_length=250)),
                ('tranche', models.CharField(choices=[('allage', 'Pour tous les âges'), ('moins40', 'Moins de 40 ans'), ('moins20', 'Moins de 20 ans'), ('plus40', 'Plus de 40 ans'), ('moins12', 'Moins de 12 ans')], max_length=250)),
                ('numero', models.CharField(max_length=250)),
                ('pantalon_type', models.CharField(choices=[('jeans', 'Pantalon Jeans'), ('jggin', 'Pantalon Jogging'), ('chino', 'Pantalon Chino'), ('tissu', 'Pantalon Tissu '), ('nilon', 'Pantalon en nilon'), ('mini', 'Pantalon en mini')], max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('taile_ecran', models.CharField(max_length=1000)),
                ('memoire', models.CharField(max_length=1000)),
                ('appareil_photo', models.CharField(max_length=1000)),
                ('systeme_exploitation', models.CharField(max_length=1000)),
                ('processeur', models.CharField(max_length=1000)),
                ('batterie', models.CharField(max_length=1000)),
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('image_face', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_dos', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_haut', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_bas', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_gauche', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_droite', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('phone_type', models.CharField(choices=[('iphone', 'Téléphone samsung'), ('iphone', 'Iphone'), ('iphone', 'Téléphone Huawei'), ('iphone', 'Téléphone oppo'), ('iphone', 'Téléphone xiomi'), ('iphone', 'Téléphone tecno'), ('iphone', 'Téléphone itel'), ('iphone', 'Téléphone HTC')], max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('slug', models.SlugField(blank=True, max_length=1000)),
                ('seller_count', models.PositiveIntegerField(default=0)),
                ('product_type', models.CharField(choices=[('men_clothing', 'Vetements'), ('women_clothing', 'Vetements'), ('men_clothing', 'Vetements'), ('clothing_accessoire', 'Accessoires de Vetements'), ('pantalon', 'Pantalon'), ('culotte', 'Culotte'), ('jupe', 'Jupe'), ('men_shoe', 'Chaussure pour homme'), ('women_shoe', 'Chaussure pour femme '), ('phone', 'Phone'), ('tablette', 'Tablette'), ('phone_accessoire', 'Accessoire de phone'), ('computer', 'Ordinateur'), ('computer_accessoire', 'Accessoire pour Ordinateur'), ('watch', 'Montre'), ('audio_viduel', 'Audio Visuel')], max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tablette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('taile_ecran', models.CharField(max_length=1000)),
                ('memoire', models.CharField(max_length=1000)),
                ('appareil_photo', models.CharField(max_length=1000)),
                ('systeme_exploitation', models.CharField(max_length=1000)),
                ('processeur', models.CharField(max_length=1000)),
                ('batterie', models.CharField(max_length=1000)),
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('image_face', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_dos', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_haut', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_bas', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_gauche', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_droite', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('tablette_type', models.CharField(choices=[('ipad', 'IPad'), ('tablette', 'Tablette')], max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tablettes', to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WomenClothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('image_derriere', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_devant', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('taille', models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=250)),
                ('genre', models.CharField(choices=[('hommes', 'Hommes'), ('femmes', 'Femmes'), ('mix', 'Mix')], max_length=250)),
                ('manche', models.CharField(choices=[('courte', 'Courte'), ('longue', 'Longue')], max_length=250)),
                ('tranche', models.CharField(choices=[('allage', 'Pour tous les âges'), ('moins40', 'Moins de 40 ans'), ('moins20', 'Moins de 20 ans'), ('plus40', 'Plus de 40 ans'), ('moins12', 'Moins de 12 ans')], max_length=250)),
                ('clothing_type', models.CharField(choices=[('shirt', 'Chemise'), ('tshirt', 'T-Shirt'), ('jacket', 'Jacket'), ('bluson', 'Bluson'), ('pull', 'Pulls'), ('polo', 'Polo'), ('maillot', 'Maillot'), ('gilet', 'Gilet'), ('robe', 'Robe'), ('pyjama', 'Pyjama'), ('tunique', 'Tunique'), ('chemisier', 'Chemisier'), ('salopette', 'Salopette')], max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='women_clothings', to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WomenShoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
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
                ('couleur', models.CharField(choices=[('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gold', 'Gold'), ('black', 'Black'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=250)),
                ('genre', models.CharField(choices=[('hommes', 'Hommes'), ('femmes', 'Femmes'), ('mix', 'Mix')], max_length=250)),
                ('tranche', models.CharField(choices=[('allage', 'Pour tous les âges'), ('moins40', 'Moins de 40 ans'), ('moins20', 'Moins de 20 ans'), ('plus40', 'Plus de 40 ans'), ('moins12', 'Moins de 12 ans')], max_length=250)),
                ('image_haut', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_dos', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_gauche', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_droite', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_derriere', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('image_devant', models.FileField(upload_to=utils.files_utils.upload_file_location)),
                ('numero', models.CharField(max_length=250)),
                ('shoes_type', models.CharField(choices=[('talon', 'Talon'), ('basket', 'Basket'), ('reposepied', 'Repose pied'), ('soulier', 'Soulier'), ('sandale', 'Sandale'), ('tenis', 'Tenis'), ('espadrille', 'Espadrille'), ('running', 'Running'), ('max', 'Chaussure max grande taille')], max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='women_shoes', to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='phone',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='products.Product'),
        ),
        migrations.AddField(
            model_name='pantalon',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pantalons', to='products.Product'),
        ),
        migrations.AddField(
            model_name='menshoes',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='men_shoes', to='products.Product'),
        ),
        migrations.AddField(
            model_name='menclothing',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='men_clothings', to='products.Product'),
        ),
        migrations.AddField(
            model_name='jupe',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jupes', to='products.Product'),
        ),
        migrations.AddField(
            model_name='culotte',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='culottes', to='products.Product'),
        ),
        migrations.AddField(
            model_name='computer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computers', to='products.Product'),
        ),
        migrations.AddField(
            model_name='accessoirephone',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessoire_phones', to='products.Product'),
        ),
        migrations.AddField(
            model_name='accessoirecomputer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accesoire_computers', to='products.Product'),
        ),
        migrations.AddField(
            model_name='accessoireclothng',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessoire_clothings', to='products.Product'),
        ),
    ]
