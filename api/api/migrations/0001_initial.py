# Generated by Django 4.2.5 on 2023-10-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RandomAlgorithmOption",
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
                ("max_project_preferences", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Requirement",
            fields=[
                (
                    "attribute_id",
                    models.CharField(
                        max_length=10, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "operator",
                    models.CharField(
                        choices=[
                            ("more than", "more than"),
                            ("less than", "less than"),
                            ("exactly", "exactly"),
                        ],
                        max_length=9,
                    ),
                ),
                ("value", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=10, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("attributes", models.JSONField(blank=True, default=dict)),
                ("relationships", models.JSONField(blank=True, default=dict)),
                ("project_preferences", models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("number_of_teams", models.IntegerField(blank=True, default=1)),
                (
                    "requirements",
                    models.ManyToManyField(blank=True, to="api.requirement"),
                ),
            ],
        ),
    ]
