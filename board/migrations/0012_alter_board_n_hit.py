# Generated by Django 4.2.2 on 2023-07-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0011_board_n_hit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="n_hit",
            field=models.IntegerField(default=0),
        ),
    ]
