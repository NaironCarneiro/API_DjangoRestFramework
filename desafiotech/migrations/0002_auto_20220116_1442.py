# Generated by Django 3.2.11 on 2022-01-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafiotech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameFruit', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
