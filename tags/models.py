from django.db import models

class Tag(models.Model):
    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True, blank=True, default=None)
    deadline = models.DateField(null=True, blank=True, default=None)
    repeatable = models.CharField(max_length=50, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name.title()}"
