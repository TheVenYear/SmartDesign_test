from rest_framework.routers import DefaultRouter

from products.views import ProductsViewSet

router = DefaultRouter()
router.register(viewset=ProductsViewSet, prefix='v1/products')

urlpatterns = router.urls
