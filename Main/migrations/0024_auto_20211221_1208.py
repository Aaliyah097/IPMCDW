# Generated by Django 3.2.6 on 2021-12-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0023_alter_industry_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='name',
        ),
        migrations.AddField(
            model_name='industry',
            name='month',
            field=models.IntegerField(choices=[('1', 'JANUARY'), ('2', 'FEBRUARY'), ('3', 'MAR')], default='1'),
        ),
    ]
