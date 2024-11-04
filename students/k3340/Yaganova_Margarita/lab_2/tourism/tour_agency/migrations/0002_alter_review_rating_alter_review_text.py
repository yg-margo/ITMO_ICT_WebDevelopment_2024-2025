# Generated by Django 4.2.16 on 2024-11-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_agency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=1000, verbose_name='Review text'),
        ),
    ]