# Generated by Django 2.2.7 on 2019-11-19 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Skits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skits',
            name='description',
            field=models.TextField(help_text="Please don't exceed 450 characters.", max_length=1000),
        ),
        migrations.AlterField(
            model_name='skits',
            name='team_group_number_1',
            field=models.ForeignKey(help_text='Please add your team first if not yet done.', on_delete=django.db.models.deletion.CASCADE, related_name='first', to='Teams.Teams'),
        ),
        migrations.AlterField(
            model_name='skits',
            name='team_group_number_2',
            field=models.ForeignKey(help_text='Please add your team first if not yet done.', on_delete=django.db.models.deletion.CASCADE, related_name='second', to='Teams.Teams'),
        ),
        migrations.AlterField(
            model_name='skits',
            name='video_url',
            field=models.CharField(help_text='Please add the embedded url link only.', max_length=100),
        ),
    ]