# Generated by Django 4.2.5 on 2023-10-04 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='team',
            new_name='active_team',
        ),
    ]