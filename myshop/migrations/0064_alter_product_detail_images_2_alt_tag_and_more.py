# Generated by Django 4.2 on 2023-04-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0063_product_detail_images_1_alt_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='images_2_ALT_TAG',
            field=models.CharField(blank=True, default='Image 2 ALT TAG', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_3_ALT_TAG',
            field=models.CharField(blank=True, default='Image 3 ALT TAG', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_4_ALT_TAG',
            field=models.CharField(blank=True, default='Image 4 ALT TAG', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_5_ALT_TAG',
            field=models.CharField(blank=True, default='Image 5 ALT TAG', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_6_ALT_TAG',
            field=models.CharField(blank=True, default='Image 6 ALT TAG', max_length=300, null=True),
        ),
    ]