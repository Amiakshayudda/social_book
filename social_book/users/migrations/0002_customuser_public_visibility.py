# Generated by Django 4.2.1 on 2023-05-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='public_visibility',
            field=models.BooleanField(default=False),
        ),
    ]
