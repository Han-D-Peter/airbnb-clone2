# Generated by Django 2.2.5 on 2020-08-26 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200825_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='rooms.Room'),
        ),
    ]
