# Generated by Django 4.0 on 2022-01-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handymanadmin', '0002_handymanadmindetails_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='handymanadmindetails',
            name='branchID',
            field=models.IntegerField(default=0),
        ),
    ]