# Generated by Django 4.1.1 on 2022-10-19 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rejestracja', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Zabawa',
        ),
    ]
