# Generated by Django 5.0 on 2023-12-09 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0002_alter_insurancecontract_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance_app.employmentcontract'),
        ),
    ]