# Generated by Django 4.1.6 on 2024-03-11 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('botanic', '0009_delete_userportfoilio'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plants', to=settings.AUTH_USER_MODEL),
        ),
    ]