# Generated by Django 4.2.1 on 2023-05-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uts', '0004_aktuatorfinal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sistem1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sistem2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sistem3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
    ]
