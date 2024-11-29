# Generated by Django 5.1.1 on 2024-11-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='target',
            field=models.CharField(blank=True, choices=[('principal', 'Principal'), ('aval', 'Aval')], max_length=10, null=True, verbose_name='Target'),
        ),
    ]
