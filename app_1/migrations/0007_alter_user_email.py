'''
Migration File
'''
# Generated by Django 5.0.1 on 2024-02-08 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    '''
    Migration Class
    '''
    dependencies = [
        ('app_1', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
