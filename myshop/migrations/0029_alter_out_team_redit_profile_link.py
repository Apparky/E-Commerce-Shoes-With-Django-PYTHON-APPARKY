# Generated by Django 3.2.18 on 2023-04-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0028_auto_20230405_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='out_team',
            name='RedIT_profile_Link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]