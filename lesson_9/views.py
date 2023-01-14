from products.models import Product, ProductCategory
from rest_framework import viewsets
from rest_framework.views import APIView
from lesson_9.serializers import ProductModelSerializer, ProductCategoryModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def func_api(request):
    print(request.data)
    return Response({'func': 'data'})


class ClassAPIView(APIView):

    def get(self, request):
        return Response({'class': 'data'}) 

    def post(self, request):
        print(request.data)
        return Response(request.data)


class ProductViewaAPISet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        s = ProductModelSerializer(self.queryset, many=True)
        return Response(s.data)

    def retrieve(self, request, pk=None):
        user = self.queryset.get(id=pk)
        s = ProductModelSerializer(user)
        return Response(s.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryModelSerializer
