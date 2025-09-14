from django.db import models

# Model for property listings
class PropertyListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    listed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title