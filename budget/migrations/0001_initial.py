# Generated by Django 4.1 on 2024-07-08 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(unique=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('always_notify', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 7, 8, 16, 42, 4, 550554))),
                ('income_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.incomecategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
