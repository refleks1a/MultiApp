# Generated by Django 4.2.5 on 2023-09-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
