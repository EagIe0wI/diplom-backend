from django.db import models

class Tag(models.Model):
    user_id = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225)
    deadline = models.DateField()
    repeatable = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name.title()}"
