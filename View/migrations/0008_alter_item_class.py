# Generated by Django 4.2.6 on 2023-10-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0007_alter_item_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Class',
            field=models.CharField(default='', max_length=100),
        ),
    ]
