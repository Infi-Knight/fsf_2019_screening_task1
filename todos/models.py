from django.db import models
from django.contrib.auth import get_user_model

# DRY
UserModel = get_user_model()


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

    # Timings
    planned_on = models.DateField(auto_now_add=True)
    completed_on = models.DateField(null=True, blank=True)
    due_on = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["planned_on"]
        verbose_name_plural = "Tasks"
