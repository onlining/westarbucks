# Generated by Django 4.0.4 on 2022-05-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_allergy_id_allergy_drink_allergy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='allergy',
            field=models.ManyToManyField(through='products.Allergy_drink', to='products.allergy'),
        ),
    ]
