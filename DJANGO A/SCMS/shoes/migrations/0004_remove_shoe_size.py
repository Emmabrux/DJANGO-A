# Generated by Django 4.1.7 on 2023-04-01 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0003_shoe_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='size',
        ),
    ]