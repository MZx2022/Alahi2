# Generated by Django 3.2.12 on 2022-03-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='User Name')),
                ('password', models.CharField(max_length=255, verbose_name='Account Password')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('otp', models.CharField(max_length=6, verbose_name='OTP')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
