# Generated by Django 4.2.11 on 2024-06-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_rename_sizes_product_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.TextField(max_length=20),
        ),
    ]