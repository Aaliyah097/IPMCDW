# Generated by Django 3.2.6 on 2021-12-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0025_auto_20211221_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(choices=[('US', 'United States'), ('FR', 'France'), ('CN', 'China'), ('RU', 'Russia'), ('IT', 'Italy')], max_length=300),
        ),
    ]
