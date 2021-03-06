# Generated by Django 3.2.7 on 2021-09-16 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("materadmin", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=256)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("junior", "Junior"),
                            ("senior", "Senior"),
                            ("teamlead", "Team Lead"),
                        ],
                        max_length=8,
                    ),
                ),
                (
                    "assign_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tasks",
                        to="materadmin.developer",
                    ),
                ),
            ],
        ),
    ]
