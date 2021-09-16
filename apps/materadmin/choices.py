from django.db import models


class DeveloperLevel(models.TextChoices):
    JUNIOR = ("junior", "Junior")
    SENIOR = ("senior", "Senior")
    TEAMLEAD = ("teamlead", "Team Lead")
