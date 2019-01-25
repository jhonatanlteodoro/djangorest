from rest_framework import routers
from .viewsets import ProductViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('product', ProductViewSet)

urlpatterns = router.urls
