# Generated by Django 4.2.6 on 2023-10-19 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0003_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrape',
            name='CurrencyID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='View.currency'),
        ),
    ]
