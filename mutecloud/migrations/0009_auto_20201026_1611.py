# Generated by Django 3.1.2 on 2020-10-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mutecloud', '0008_auto_20201026_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Unrated'), (1, 'Flop'), (2, 'Fade'), (3, 'Average'), (4, 'Classic'), (5, 'All Time')], default=0),
        ),
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Unrated'), (1, 'Flop'), (2, 'Fade'), (3, 'Average'), (4, 'Classic'), (5, 'All Time')], default=0),
        ),
    ]
