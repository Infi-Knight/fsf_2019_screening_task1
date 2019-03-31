import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# DRY
UserModel = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(default='', max_length=1024, blank=True)
    leader = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name='leads_teams')
    members = models.ManyToManyField(UserModel)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("task_manager:team_description", kwargs={"team_id": self.id})

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Teams"


class Task(models.Model):
    PLANNED = 'Planned'
    INPROGRESS = 'Inprogress'
    DONE = 'Done'
    TASK_PHASE = (
        (PLANNED, 'Planned'),
        (INPROGRESS, 'In progress'),
        (DONE, 'Done'),
    )

    title = models.CharField(max_length=50)
    desc = models.TextField(default="", blank=True)
    status = models.CharField(
        max_length=10, choices=TASK_PHASE, default='PLANNED')

    # related_name specifies a reverse relationship
    creator = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name='created_tasks')

    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True)

    member_assigned = models.ManyToManyField(
        UserModel, help_text="Select members to assign this task to")

    # Timings
    planned_on = models.DateField(auto_now_add=True)
    completed_on = models.DateField(null=True, blank=True)
    due_on = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_manager:task_description", kwargs={"task_id": self.id})

    def has_duedate_passed(self):
        """Returns whether the Tasks's due date has passed or not."""
        if self.due_on and datetime.date.today() > self.due_on:
            return True
        else:
            return False

    class Meta:
        ordering = ["planned_on"]
        verbose_name_plural = "Tasks"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def comment_info(self):
        return "@{author}: {comment_info}...".format(author=self.author, comment_info=self.comment[:50])

    def __str__(self):
        return self.comment_info()

    class Meta:
        ordering = ["-timestamp"]
