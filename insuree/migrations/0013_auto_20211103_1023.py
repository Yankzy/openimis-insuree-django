# Generated by Django 3.0.14 on 2021-11-03 10:23
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("insuree", "0012_policyrenewaldetail"),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE NONCLUSTERED INDEX ix_tblInsuree_validity ON [dbo].[tblInsuree]
            (
                [ValidityFrom] ASC,
                [LegacyID] ASC,
                InsureeID
            )""" if settings.MSSQL else """
            CREATE INDEX "ix_tblInsuree_validity" ON "tblInsuree"
            (
                "ValidityFrom" ASC,
                "LegacyID" ASC,
                "InsureeID"
            )""",
            reverse_sql='DROP index "ix_tblInsuree_validity" on "tblInsuree"',
        )
    ]
