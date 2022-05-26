# Generated by Django 3.2.12 on 2022-05-19 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('accounts', '0002_user_watched_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='like_movies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='watched_movies',
        ),
        migrations.AlterField(
            model_name='userlikeactor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_actor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userlikedirector',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_direcor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserWatchedMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie_watched_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watched', to='movies.movie')),
                ('user_watched_movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_watched', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikeMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie_like_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_like', to='movies.movie')),
                ('user_like_movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]