# Generated by Django 2.2.1 on 2019-05-23 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='release_date',
            new_name='rldate',
        ),
    ]