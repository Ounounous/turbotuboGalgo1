# Generated by Django 5.1.1 on 2024-11-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demographics', '0010_alter_avaldemographics_aval_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaldemographics',
            name='aval_rut',
            field=models.CharField(max_length=15),
        ),
    ]
