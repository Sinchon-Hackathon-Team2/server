# Generated by Django 4.2.4 on 2023-08-25 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("content", models.TextField()),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("ballad_tag", models.BooleanField(default=False)),
                ("dance_tag", models.BooleanField(default=False)),
                ("rap_tag", models.BooleanField(default=False)),
                ("RandB_tag", models.BooleanField(default=False)),
                ("indie_tag", models.BooleanField(default=False)),
                ("rock_tag", models.BooleanField(default=False)),
                (
                    "music_name1",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url1", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name2",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url2", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name3",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url3", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name4",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url4", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name5",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url5", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name6",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url6", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name7",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url7", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name8",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url8", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name9",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("music_url9", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "music_name10",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "music_url10",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "univ_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="account.univ"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="account.user"
                    ),
                ),
            ],
        ),
    ]
