# Generated by Django 4.2.5 on 2023-09-15 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('lead', '0002_lead_converted_to_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='team.team'),
            preserve_default=False,
        ),
    ]
