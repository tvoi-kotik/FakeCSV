# Generated by Django 3.1.4 on 2020-12-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvgen', '0002_auto_20201213_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemas',
            name='Column_separator',
            field=models.CharField(default='Comma (,)', max_length=50),
        ),
        migrations.AddField(
            model_name='schemas',
            name='String_character',
            field=models.CharField(default='Double-quote (")', max_length=50),
        ),
    ]