# Generated by Django 2.2 on 2019-05-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0030_doctors_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='tel_no',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
