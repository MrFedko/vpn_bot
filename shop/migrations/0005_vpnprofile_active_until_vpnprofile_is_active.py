# Generated by Django 4.1.5 on 2023-01-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_vpnserver_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpnprofile',
            name='active_until',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='vpnprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]