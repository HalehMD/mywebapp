# Generated by Django 2.1.3 on 2022-07-11 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220711_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='course',
        ),
        migrations.AddField(
            model_name='order',
            name='course',
            field=models.ForeignKey(default='000', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myapp.Course'),
        ),
    ]
