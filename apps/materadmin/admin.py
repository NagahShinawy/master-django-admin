from django.contrib import admin
from .models import Developer, Task


class DeveloperSiteArea(admin.AdminSite):
    site_header = "Developer Dashboard"


class TaskSiteArea(admin.AdminSite):
    site_header = "Tasks Dashboard"


developer_site = DeveloperSiteArea(name="DeveloperSite")
task_site = TaskSiteArea(name="TaskSite")
developer_site.register(Developer)
task_site.register(Task)

admin.site.register(Developer)
