# Generated by Django 3.1.2 on 2022-04-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_otp_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='confirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation', models.CharField(max_length=4)),
            ],
        ),
    ]
