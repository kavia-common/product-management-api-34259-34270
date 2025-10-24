from rest_framework import serializers
from .models import Product


# PUBLIC_INTERFACE
class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model with basic validation."""

    class Meta:
        model = Product
        fields = ["id", "name", "price", "quantity", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_name(self, value: str) -> str:
        """Ensure product name is not blank and has a reasonable length."""
        if not value or not value.strip():
            raise serializers.ValidationError("Name cannot be blank.")
        if len(value.strip()) > 255:
            raise serializers.ValidationError("Name must be at most 255 characters.")
        return value.strip()

    def validate(self, attrs):
        """Cross-field validations (if any)."""
        price = attrs.get("price", getattr(self.instance, "price", None))
        quantity = attrs.get("quantity", getattr(self.instance, "quantity", None))
        if price is not None and price < 0:
            raise serializers.ValidationError({"price": "Price cannot be negative."})
        if quantity is not None and quantity < 0:
            raise serializers.ValidationError({"quantity": "Quantity cannot be negative."})
        return attrs
