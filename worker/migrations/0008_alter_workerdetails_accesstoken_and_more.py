# Generated by Django 4.0 on 2022-01-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0007_alter_workerdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerdetails',
            name='accessToken',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
