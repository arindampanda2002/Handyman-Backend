# Generated by Django 4.0 on 2022-01-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handymanadmin', '0005_alter_handymanadmindetails_statename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handymanadmindetails',
            name='branchId',
            field=models.IntegerField(),
        ),
    ]
