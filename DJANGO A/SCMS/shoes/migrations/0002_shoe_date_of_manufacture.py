# Generated by Django 4.1.7 on 2023-04-01 17:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='date_of_manufacture',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
