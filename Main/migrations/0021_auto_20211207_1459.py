# Generated by Django 3.2.6 on 2021-12-07 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0020_alter_user_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postal_code',
            new_name='zipcode',
        ),
    ]
