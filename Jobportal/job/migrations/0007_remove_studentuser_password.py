# Generated by Django 3.2.4 on 2023-04-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_studentuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='password',
        ),
    ]
