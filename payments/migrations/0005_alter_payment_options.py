# Generated by Django 3.2.4 on 2022-04-07 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20220403_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name_plural': 'Customer Bill Payments Status'},
        ),
    ]