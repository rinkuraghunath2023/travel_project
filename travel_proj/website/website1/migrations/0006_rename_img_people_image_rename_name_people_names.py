# Generated by Django 4.1.5 on 2023-02-01 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0005_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='names',
        ),
    ]
