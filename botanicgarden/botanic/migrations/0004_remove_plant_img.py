# Generated by Django 4.1.6 on 2024-03-08 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botanic', '0003_alter_plant_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='img',
        ),
    ]