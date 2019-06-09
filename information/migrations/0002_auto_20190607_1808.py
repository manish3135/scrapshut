# Generated by Django 2.1.7 on 2019-06-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='branch_choice',
            field=models.CharField(choices=[('CSE', 'computer '), ('ECE', 'electrical '), ('ME', 'mechanical'), ('CIVIL', 'civil'), ('EEE', 'electronics')], default=None, max_length=15),
        ),
    ]