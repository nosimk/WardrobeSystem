# Generated by Django 5.1.6 on 2025-03-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_user_wardrobe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wardrobe',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
