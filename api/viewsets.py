from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.utils.serializer_helpers import ReturnList

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    api_version = 'api/v1'

    def add_refs_to_item_list(self, orderdict):
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
                },
                {
                    "rel": "self",
                    "href": f"{self.api_version}/product/{item['id']}",
                    "type" : "PUT"
                },
            ]
        return orderdict

    def add_refs_to_item(self, data):
        data.data['link'] = [
            {
                "rel": "self",
                "href": f"{self.api_version}/product/{data.data['id']}",
                "type" : "DELETE"
            },
            {
                "rel": "self",
                "href": f"{self.api_version}/product/{data.data['id']}",
                "type" : "PUT"
            },
            {
                "rel": "self",
                "href": f"{self.api_version}/product/{data.data['id']}",
                "type" : "PATCH"
            }
        ]
        return data

    def list(self, request):
        data_default = super(ProductViewSet, self).list(request)
        return self.add_refs_to_item_list(data_default)

    def partial_update(self, request, pk=None):
        data_default = super(ProductViewSet, self).partial_update(request, pk)
        return self.add_refs_to_item(data_default)

    def retrieve(self, request, pk=None):
        data_default = super(ProductViewSet, self).retrieve(request, pk)
        return self.add_refs_to_item(data_default)
