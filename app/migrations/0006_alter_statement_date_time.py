# Generated by Django 5.0.6 on 2024-05-22 20:24

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_statement_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='date_time',
            field=models.DateTimeField(validators=[app.models.statement_date_time_only_hours], verbose_name='Дата и время'),
        ),
    ]
