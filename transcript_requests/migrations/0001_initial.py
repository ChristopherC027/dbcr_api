# Generated by Django 2.2 on 2020-05-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('classYear', models.CharField(max_length=100)),
                ('emailAddress', models.CharField(max_length=100)),
                ('needDate', models.DateField()),
                ('vInstCompName', models.CharField(blank=True, default='', max_length=100)),
                ('instCompEmail', models.CharField(blank=True, default='', max_length=100)),
                ('pInstCompName', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('zip', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]