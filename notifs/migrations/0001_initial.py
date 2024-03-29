# pylint: disable=invalid-name

'''
Migration file for Notification
'''

# Generated by Django 4.2.10 on 2024-03-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    '''
    Migration Class
    '''

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastNotification',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),

                ('message', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sent', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
