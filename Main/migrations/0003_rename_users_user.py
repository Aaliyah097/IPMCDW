# Generated by Django 3.2.6 on 2021-11-18 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_rename_user_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
