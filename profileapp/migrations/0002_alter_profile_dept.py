# Generated by Django 3.2.3 on 2021-05-25 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dept',
            field=models.CharField(choices=[('not-specified', 'Not Specified'), ('uplex', 'UPLEX'), ('mju', 'MJU')], max_length=100, null=True),
        ),
    ]