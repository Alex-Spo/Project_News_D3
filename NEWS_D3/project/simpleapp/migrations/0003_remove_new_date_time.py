# Generated by Django 4.0.2 on 2022-02-09 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_new_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='date_time',
        ),
    ]
