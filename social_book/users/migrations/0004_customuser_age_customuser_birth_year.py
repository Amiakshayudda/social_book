# Generated by Django 4.2.1 on 2023-05-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_city_customuser_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth_year',
            field=models.IntegerField(default=0),
        ),
    ]