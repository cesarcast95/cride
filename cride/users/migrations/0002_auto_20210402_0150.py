# Generated by Django 3.1.7 on 2021-04-02 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_verfied',
            new_name='is_verified',
        ),
    ]
