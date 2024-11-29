# Generated by Django 5.1.1 on 2024-10-29 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demographics', '0008_phone_lead'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaldemographics',
            old_name='address',
            new_name='aval_address',
        ),
        migrations.RenameField(
            model_name='avaldemographics',
            old_name='dv_aval',
            new_name='aval_dv',
        ),
        migrations.RenameField(
            model_name='avaldemographics',
            old_name='email',
            new_name='aval_email',
        ),
        migrations.RenameField(
            model_name='avaldemographics',
            old_name='nombre_aval',
            new_name='aval_name',
        ),
        migrations.RenameField(
            model_name='avaldemographics',
            old_name='rut_aval',
            new_name='aval_rut',
        ),
        migrations.RenameField(
            model_name='iddemographics',
            old_name='address',
            new_name='principal_address',
        ),
        migrations.RenameField(
            model_name='iddemographics',
            old_name='email',
            new_name='principal_email',
        ),
    ]
