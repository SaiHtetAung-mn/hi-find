# Generated by Django 4.2.4 on 2023-09-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lostusers',
            options={},
        ),
        migrations.AlterModelManagers(
            name='lostusers',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='lostusers',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='lostusers',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
