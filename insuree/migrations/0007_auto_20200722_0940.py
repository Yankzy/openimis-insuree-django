# Generated by Django 3.0.3 on 2020-07-22 09:40
from django.conf import settings

import core.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_healthfacilitycatchment_healthfacilitylegalform_healthfacilitymutation_healthfacilitysublevel'),
        ('insuree', '0006_auto_20200722_0839'),
    ]

    operations = [
        # not picked up (because managed = False?)
        # migrations.AlterField(
        #     model_name='insuree',
        #     name='current_village',
        #     field=models.ForeignKey(blank=True, db_column='CurrentVillage', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.Location')
        # ),
        # so let's make it raw SQL...
        migrations.RunSQL(
            "ALTER TABLE [tblInsuree] ADD CONSTRAINT "
            "[tblInsuree_CurrentVillage_8ea25085_fk_tblLocations_LocationId] "
            "FOREIGN KEY([CurrentVillage]) REFERENCES[tblLocations]([LocationId]);"
            if settings.MSSQL else
            'ALTER TABLE "tblInsuree" ADD CONSTRAINT "tblInsuree_CurrentVillage_8ea25085_fk_tblLocations_LocationId" '
            ' FOREIGN KEY("CurrentVillage") REFERENCES "tblLocations"("LocationId");'
        )

    ]
