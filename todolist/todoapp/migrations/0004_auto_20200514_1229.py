# Generated by Django 3.0.3 on 2020-05-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todolistitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
