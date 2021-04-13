from django.db import models
from company.models import Company
from user.models import User


class Project(models.Model):
    uuid = models.UUIDField(auto_created=True)
    company = models.ForeignKey(
        Company,
        related_name="projects",
        on_delete=models.PROTECT,
    )
    created_user = models.ForeignKey(
        User,
        related_name="created_projects",
        on_delete=models.PROTECT,
    )
    is_archived = models.BooleanField(default=False)
    date_time_created = models.DateTimeField(auto_now_add=True)


class ProjectLanguage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="languages",
        on_delete=models.PROTECT,
    )
    tag = models.CharField(max_length=10)
    created_user = models.ForeignKey(
        User,
        related_name="created_project_languages",
        on_delete=models.PROTECT,
    )
    date_time_created = models.DateTimeField(auto_now_add=True)
