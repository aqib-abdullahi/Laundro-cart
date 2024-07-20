from django.db import models

class Category(models.Model):
    """Category models"""
    name = models.CharField(max_length=50)

    @staticmethod
    def get_categories():
        """returns all categories"""
        return Category.objects.all()

    def __str__(self):
        return self.name