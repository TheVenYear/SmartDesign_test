from rest_framework.routers import DefaultRouter

from products.views import ProductsViewSet

router = DefaultRouter()
router.register(viewset=ProductsViewSet, prefix='')

urlpatterns = router.urls
