# Generated by Django 3.1.4 on 2020-12-12 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schemas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('Post_date', models.DateField()),
                ('Full_name', models.BooleanField(default=False)),
                ('Job', models.BooleanField(default=False)),
                ('Email', models.BooleanField(default=False)),
                ('Domain_name', models.BooleanField(default=False)),
                ('Phone_number', models.BooleanField(default=False)),
                ('Company_name', models.BooleanField(default=False)),
                ('Text', models.BooleanField(default=False)),
                ('Text_number', models.IntegerField()),
                ('Integer', models.BooleanField(default=False)),
                ('Integer_range_from', models.IntegerField()),
                ('Integer_range_to', models.IntegerField()),
                ('Address', models.BooleanField(default=False)),
                ('Date_field', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
