# Generated by Django 4.2.5 on 2024-04-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_table_remove_reservation_date_reservation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_number',
            field=models.CharField(max_length=50),
        ),
    ]
