# Generated by Django 4.2.6 on 2024-03-18 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
