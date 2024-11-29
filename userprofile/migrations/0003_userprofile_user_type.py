# Generated by Django 5.1.1 on 2024-11-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_active_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('owner', 'Owner'), ('supervisor', 'Supervisor'), ('collector', 'Collector')], default='collector', max_length=10),
        ),
    ]