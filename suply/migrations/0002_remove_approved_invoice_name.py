# Generated by Django 4.1.3 on 2023-01-27 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suply', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approved_invoice',
            name='name',
        ),
    ]
