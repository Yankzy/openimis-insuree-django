# Generated by Django 3.0.3 on 2020-07-31 04:43
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0007_auto_20200722_0940'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE[tblInsuree] ALTER COLUMN FamilyID [int] NULL;"
            if settings.MSSQL else
            'ALTER TABLE "tblInsuree" ALTER COLUMN "FamilyID" DROP NOT NULL;'
        )
    ]
