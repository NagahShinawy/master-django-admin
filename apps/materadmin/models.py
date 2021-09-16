from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=256)
    assign_to = models.ForeignKey("Developer", related_name="tasks", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Developer(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name