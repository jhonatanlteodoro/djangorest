from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.test.client import RequestFactory
from .models import Product
from .viewsets import ProductViewSet

class ApiTests(APITestCase):

    def setUp(self):
        """
        Criando objetos para teste
        """
        Product.objects.bulk_create([
            Product(name='NoteTest1', category='notebooks'),
            Product(name='Moto z2 Play', category='smartphone'),
            Product(name='Moto z3 Play', category='smartphone'),
        ])

    def test_get_list(self):
        """
        Teste endpoint para listagem de produtos criados
        """
        view = ProductViewSet.as_view({'get': 'list'})
        factory = RequestFactory()
        request = factory.get('api/v1/product')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_len_products_created(self):
        """
        Teste para verificar se a quantidade de items criados é igual ao
        setUp inicial
        """
        view = ProductViewSet.as_view({'get': 'list'})
        factory = RequestFactory()
        request = factory.get('api/v1/product')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_links_product_refs(self):
        """
        Verificando se a listagem de produtos está vindo com os links de
        referência
        """
        view = ProductViewSet.as_view({'get': 'list'})
        factory = RequestFactory()
        request = factory.get('api/v1/product')
        response = view(request)
        for item in response.data:
            self.assertNotEqual(item.get('links'), None)

    def test_get_product_and_delete_with_link_ref_delete(self):
        """
        Verificando se a listagem de produtos está vindo com os links de
        referência e deletando cada um deles
        """
        view = ProductViewSet.as_view({'get': 'list'})
        factory = RequestFactory()
        request = factory.get('api/v1/product')
        response = view(request)
        for item in response.data:
            for link in item.get('links'):
                if link.get('type') == 'DELETE':
                    view = ProductViewSet.as_view({'delete': 'destroy'})
                    request = factory.delete(link.get('href'))
                    response = view(request, pk=item.get('id'))
                    self.assertEqual(
                        response.status_code,
                        status.HTTP_204_NO_CONTENT
                    )
        #verificando os produtos foram realmente deletados
        view = ProductViewSet.as_view({'get': 'list'})
        request = factory.get('api/v1/product')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


    def test_get_list_product_and_update_prodcut_with_link_ref_patch(self):
        """
        Testando link de referêcia http PATCH para update dos produtos
        """
        view = ProductViewSet.as_view({'get': 'list'})
        factory = RequestFactory()
        request = factory.get('api/v1/product')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) == 3)
        list_update = [
            {"name": "prod update1", "category": "smartphone"},
            {"name": "prod update2", "category": "notebooks"},
            {"name": "prod update3", "category": "smartphone"},
        ]

        factory = APIRequestFactory()
        for i, item in enumerate(response.data):
            for link in item.get('links'):
                if link.get('type') == 'PATCH':
                    view = ProductViewSet.as_view({'patch': 'partial_update'})
                    # import pdb; pdb.set_trace()
                    request = factory.patch(
                        link.get('href'),
                        list_update[i],
                        format='json'
                    )
                    response = view(request, pk=item.get('id'))

        #validando alterações
        view = ProductViewSet.as_view({'get': 'list'})
        factory = RequestFactory()
        request = factory.get('api/v1/product')
        response = view(request)
        for i, item in enumerate(response.data):
            self.assertEqual(item['name'], list_update[i]['name'])
            self.assertEqual(item['category'], list_update[i]['category'])
