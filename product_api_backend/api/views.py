from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, pagination
from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def health(request):
    """Simple healthcheck endpoint."""
    return Response({"message": "Server is up!"})


class DefaultPageNumberPagination(pagination.PageNumberPagination):
    """Default paginator using settings or sensible defaults."""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# PUBLIC_INTERFACE
class ProductListCreateView(generics.ListCreateAPIView):
    """
    List and Create Products.

    GET /api/products/:
      - Returns a paginated list of products.
      - Query params:
          - page: page number (default 1)
          - page_size: items per page (default 10, max 100)

    POST /api/products/:
      - Create a product.
      - Body:
          {
            "name": "Sample",
            "price": 19.99,
            "quantity": 5
          }
    """
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    pagination_class = DefaultPageNumberPagination


# PUBLIC_INTERFACE
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, or Delete a Product by ID.

    GET /api/products/{id}/
    PUT /api/products/{id}/
    PATCH /api/products/{id}/
    DELETE /api/products/{id}/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


# PUBLIC_INTERFACE
@api_view(['GET'])
def total_inventory_balance(request):
    """
    Calculate and return the total inventory balance.

    This endpoint returns the sum of price * quantity across all Product records.
    Decimal-safe arithmetic is used by leveraging a DecimalField in the aggregation.

    GET /api/products/total-balance/
    Response:
      {
        "total_balance": "<decimal_string>"
      }

    Note: The value is a monetary/amount total, but currency is not enforced or hardcoded.
    """
    # Ensure Decimal-safe arithmetic: wrap the multiplication with a DecimalField
    total = Product.objects.aggregate(
        total_balance=Sum(
            ExpressionWrapper(
                F('price') * F('quantity'),
                output_field=DecimalField(max_digits=20, decimal_places=2),
            )
        )
    )['total_balance'] or 0

    # DRF JSONRenderer will serialize Decimal to string by default with JSONEncoder.
    return Response({"total_balance": total})
