# Generated by Django 3.1.7 on 2021-04-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_district_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='district',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='price_with_all_facility',
            field=models.FloatField(default=0),
        ),
    ]
