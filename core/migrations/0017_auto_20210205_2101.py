# Generated by Django 3.1.5 on 2021-02-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210205_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Photo'),
        ),
    ]
