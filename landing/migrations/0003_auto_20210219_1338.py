# Generated by Django 3.1.6 on 2021-02-19 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20210219_1337'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
    ]