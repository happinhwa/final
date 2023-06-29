# Generated by Django 4.2 on 2023-06-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.IntegerField()),
                ('following', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'genres2',
            },
        ),
        migrations.CreateModel(
            name='Mypage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.DecimalField(decimal_places=2, max_digits=65)),
                ('visit_count', models.IntegerField()),
                ('profile_img', models.ImageField(null=True, upload_to='profiles/')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.IntegerField()),
                ('birth', models.DateField()),
                ('fav_genre', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
