from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Product model representing an item with a name, price and quantity.
    """
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Price must be a non-negative value with up to 2 decimal places.",
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Quantity must be a non-negative integer.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.name} (${self.price}) x{self.quantity}"
