# Generated by Django 4.2.7 on 2023-11-06 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("cpassword", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_title", models.CharField(max_length=20)),
                ("posts", models.CharField(max_length=200)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=20)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LikeButton",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(null=True)),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="likes", to="user.user"
                    ),
                ),
            ],
        ),
    ]
