# Generated by Django 3.2.18 on 2023-03-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0021_auto_20230324_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='insuree',
            name='nin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='insuree',
            name='uin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
