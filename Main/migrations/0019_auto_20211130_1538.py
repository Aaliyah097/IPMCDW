# Generated by Django 3.2.6 on 2021-11-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0018_rename_second_name_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(default='EUR', max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default=1, max_length=20),
        ),
    ]