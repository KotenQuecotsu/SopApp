# Generated by Django 4.2 on 2023-04-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subname', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('birth_date', models.DateField(verbose_name='Время рождения')),
            ],
        ),
    ]
