# Generated by Django 3.2.18 on 2023-04-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0039_auto_20230406_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_page_heading', models.CharField(max_length=400)),
                ('blog_page_sub_heading', models.CharField(max_length=700)),
                ('blog_meta_data', models.CharField(max_length=300)),
                ('blog_image', models.FileField(upload_to='midea/images/')),
                ('blog_image_ALT_TAG', models.CharField(max_length=350)),
            ],
        ),
    ]
