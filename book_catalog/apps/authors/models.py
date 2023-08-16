from django.db import models


class Author(models.Model):
    """
    Model for Author
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f"{self.first_name}   {self.last_name}"
