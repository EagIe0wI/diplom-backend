from django.db import models

class Event(models.Model):
    card = models.ForeignKey(
        'cards.Card',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True, blank=True, default=None)
    date_happened = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title.title()}"
