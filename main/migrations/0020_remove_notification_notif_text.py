# Generated by Django 4.1 on 2022-08-11 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notif_text',
        ),
    ]