# Generated by Django 3.2.6 on 2021-12-24 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0033_alter_user_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.user')),
            ],
        ),
    ]
