# Generated by Django 4.2 on 2023-04-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0064_alter_product_detail_images_2_alt_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='product_status',
            field=models.CharField(choices=[('a', 'Available'), ('un', 'UnAvailable')], default='a', max_length=60),
        ),
    ]
