# Generated by Django 3.2.6 on 2021-12-21 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0024_auto_20211221_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='month',
        ),
        migrations.AddField(
            model_name='industry',
            name='name',
            field=models.CharField(choices=[('1', 'JANUARY'), ('2', 'FEBRUARY'), ('3', 'MAR')], default='1', max_length=1),
        ),
    ]