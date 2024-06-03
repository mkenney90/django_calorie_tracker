from django.db import models

class CalorieEntry(models.Model):
    date = models.DateField()
    food_item = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.food_item} - {self.calories} kcal on {self.date}"
