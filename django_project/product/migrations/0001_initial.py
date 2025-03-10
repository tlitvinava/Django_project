# Generated by Django 5.1 on 2025-02-16 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('storage_methods', models.CharField(max_length=30)),
                ('vitamins', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('expiration_date', models.DateField()),
                ('appearance', models.CharField(max_length=30)),
                ('proteins', models.CharField(max_length=30)),
                ('fats', models.CharField(max_length=30)),
                ('carbohydrates', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
            ],
        ),
    ]
