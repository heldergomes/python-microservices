# Generated by Django 5.0.1 on 2024-02-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_product_description_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]