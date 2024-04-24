# Generated by Django 4.1 on 2024-03-19 18:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                (
                    "create_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024,
                            3,
                            19,
                            18,
                            33,
                            38,
                            237547,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                ("published_date", models.DateTimeField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("author", models.CharField(max_length=200)),
                ("text", models.TextField()),
                (
                    "create_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024,
                            3,
                            19,
                            18,
                            33,
                            38,
                            237547,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                ("approved_comment", models.BooleanField(default=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
        ),
    ]
