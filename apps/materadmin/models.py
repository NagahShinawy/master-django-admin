from django.db import models
from .choices import DeveloperLevels


class Task(models.Model):
    title = models.CharField(max_length=256)
    assign_to = models.ForeignKey(
        "Developer", related_name="tasks", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title


class Developer(models.Model):
    name = models.CharField(max_length=256, verbose_name="Developer Name")
    level = models.CharField(
        max_length=8, choices=DeveloperLevels.choices, default=DeveloperLevels.SENIOR,
        verbose_name="Exp Level",
    )
    salary = models.IntegerField(null=True, blank=True, verbose_name="Dev Salary")

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField(null=True, blank=True)
