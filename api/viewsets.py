from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    api_version = 'api/v1'

    def add_refs_to_items(self, orderdict):
        for item in orderdict.data:
            item["links"] = [
                {
                    "rel": "self",
                    "href": f"{self.api_version}/product/{item['id']}",
                    "type" : "GET"
                },
                {
                    "rel": "self",
                    "href": f"{self.api_version}/product/{item['id']}",
                    "type" : "DELETE"
                },
                {
                    "rel": "self",
                    "href": f"{self.api_version}/product/{item['id']}",
                    "type" : "PATCH"
                }
            ]
        return orderdict

    def list(self, request):
        data_default = super(ProductViewSet, self).list(request)
        return self.add_refs_to_items(data_default)
