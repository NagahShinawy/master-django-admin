from django.db import models


class DeveloperLevels(models.TextChoices):
    JUNIOR = ("junior", "Junior")
    SENIOR = ("senior", "Senior")
    TEAMLEAD = ("teamlead", "Team Lead")
