# Generated by Django 4.2 on 2023-04-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=40, null=True, verbose_name='Key')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
    ]
