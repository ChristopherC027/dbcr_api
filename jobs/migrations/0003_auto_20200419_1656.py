# Generated by Django 2.2 on 2020-04-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200127_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expires_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='posted_at',
            field=models.DateField(),
        ),
    ]
