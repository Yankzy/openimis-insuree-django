# Generated by Django 3.2.18 on 2023-03-26 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0023_alter_insuree_audit_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuree',
            name='audit_user_id',
            field=models.IntegerField(db_column='AuditUserID'),
        ),
    ]