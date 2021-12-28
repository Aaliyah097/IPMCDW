# Generated by Django 3.2.6 on 2021-12-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0030_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Visitor'), (2, 'User'), (3, 'Premium'), (4, 'Vip'), (4, 'Admin')]),
        ),
    ]