# Generated by Django 4.2.5 on 2024-04-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_table_is_available_alter_table_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(),
        ),
    ]
