# Generated by Django 3.2.4 on 2022-09-10 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_mcart_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='ppic',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]