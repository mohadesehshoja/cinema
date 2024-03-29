# Generated by Django 5.0.2 on 2024-03-01 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickting', '0002_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('salable_seats', models.IntegerField()),
                ('free_seats', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'sale not started'), (2, 'sale opened'), (3, 'tickets sold'), (4, 'sale closed'), (5, 'movie played'), (6, 'show cancelled')])),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickting.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickting.movie')),
            ],
        ),
    ]