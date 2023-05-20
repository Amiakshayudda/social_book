# Generated by Django 4.2.1 on 2023-05-18 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_age_customuser_birth_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('visibility', models.BooleanField(default=True)),
                ('cost', models.IntegerField()),
                ('year_of_publishing', models.IntegerField()),
                ('cover_image', models.ImageField(upload_to='book_cover/')),
                ('book_path', models.FileField(upload_to='book/')),
                ('CustomUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
