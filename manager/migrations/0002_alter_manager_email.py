# Generated by Django 3.2.8 on 2022-10-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
