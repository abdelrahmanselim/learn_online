# Generated by Django 4.1 on 2022-08-10 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_courserating'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='teacher_profile_imgs/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]