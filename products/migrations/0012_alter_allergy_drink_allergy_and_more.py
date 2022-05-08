# Generated by Django 4.0.4 on 2022-05-07 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_drinks_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy_drink',
            name='allergy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy'),
        ),
        migrations.AlterField(
            model_name='allergy_drink',
            name='drinks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks'),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='allergyed',
            field=models.ManyToManyField(through='products.Allergy_drink', to='products.allergy'),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
    ]
