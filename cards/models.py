from django.db import models

class Card(models.Model):
    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.title.title()}"

class ExtraFieldForCard(models.Model):
    card = models.ForeignKey(
        "Card",
        on_delete=models.CASCADE,
    )
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=225)
    typeOfValue = models.ForeignKey(
        "TypeField",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.task_id} {self.key}"

class TypeField(models.Model):
    value = models.CharField(max_length=50)
    displayName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.displayName.title()}"
