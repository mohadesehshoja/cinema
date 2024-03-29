# Generated by Django 5.0.2 on 2024-03-27 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='amount')),
                ('transaction_time', models.DateTimeField(auto_now_add=True, verbose_name='time')),
                ('transaction_id', models.CharField(max_length=30, verbose_name='transaction id')),
                ('myprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile', verbose_name='your profile')),
            ],
        ),
    ]
