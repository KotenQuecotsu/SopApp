# Generated by Django 4.2 on 2023-04-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sopapp', '0003_alter_person_birth_date_delete_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
