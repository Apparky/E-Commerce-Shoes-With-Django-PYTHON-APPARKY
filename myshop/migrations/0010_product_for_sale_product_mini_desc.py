# Generated by Django 3.2.18 on 2023-04-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0009_remove_contact_us_cust_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_for_sale',
            name='product_mini_desc',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
