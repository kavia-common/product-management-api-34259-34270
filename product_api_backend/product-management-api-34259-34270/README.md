# product-management-api-34259-34270

Backend: Django + Django REST Framework

- Live docs (Swagger): /docs
- Redoc: /redoc
- OpenAPI JSON: /swagger.json
- Health: GET /api/health/

Products API
- List/Create: 
  - GET /api/products/
  - POST /api/products/
- Retrieve/Update/Delete:
  - GET /api/products/{id}/
  - PUT /api/products/{id}/
  - PATCH /api/products/{id}/
  - DELETE /api/products/{id}/
- Total Inventory Balance:
  - GET /api/products/total-balance/ -> {"total_balance":"<decimal>"}
    - Note: total_balance represents a monetary/amount total; the currency unit depends on your system configuration and is not hardcoded here.

Validation
- name: required, non-blank, max 255, unique
- price: decimal >= 0
- quantity: integer >= 0

Pagination
- PageNumberPagination; query params: ?page=1&page_size=10 (max 100)

Example curl
- Create:
  curl -s -X POST http://localhost:3001/api/products/ \
    -H "Content-Type: application/json" \
    -d '{"name":"Pen","price":1.99,"quantity":100}'

- List:
  curl -s http://localhost:3001/api/products/

- Retrieve:
  curl -s http://localhost:3001/api/products/1/

- Update:
  curl -s -X PUT http://localhost:3001/api/products/1/ \
    -H "Content-Type: application/json" \
    -d '{"name":"Blue Pen","price":2.49,"quantity":150}'

- Partial Update:
  curl -s -X PATCH http://localhost:3001/api/products/1/ \
    -H "Content-Type: application/json" \
    -d '{"quantity":200}'

- Delete:
  curl -s -X DELETE http://localhost:3001/api/products/1/

- Total Inventory Balance:
  curl -s http://localhost:3001/api/products/total-balance/

Notes
- No environment variables are required for basic usage; SQLite is used by default.
- The API is served automatically by the preview environment.
