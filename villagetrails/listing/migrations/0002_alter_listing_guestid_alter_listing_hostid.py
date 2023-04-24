# Generated by Django 4.2 on 2023-04-24 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='guestId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guest_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='hostId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='host_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
