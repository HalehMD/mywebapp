# Generated by Django 4.0.4 on 2022-05-30 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_order_n'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='n',
        ),
    ]