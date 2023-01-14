from django.urls import include, path
from rest_framework import routers
from lesson_9 import views

router = routers.SimpleRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'category', views.ProductCategoryViewSet)
router.register(r'product-set', views.ProductViewaAPISet)

urlpatterns = [
    path('', include(router.urls)),
    path('func-api/', views.func_api),
    path('class-api/', views.ClassAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
