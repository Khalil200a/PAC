# Generated by Django 2.2.6 on 2021-08-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_produit_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image10',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
