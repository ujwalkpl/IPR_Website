# Generated by Django 2.2.7 on 2019-11-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0004_auto_20191119_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='group_photo',
            field=models.ImageField(default='default.jpg', help_text='Preferrably landscape pictures.', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_number',
            field=models.CharField(help_text='Format: Team 1, Team 2 etc..', max_length=100),
        ),
    ]