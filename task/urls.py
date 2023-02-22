from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task.views import ItemModelViewSet, ItemStripeAPIView, items, items_detail

# router = DefaultRouter()
# router.register('item', ItemModelViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('create-session', ItemStripeAPIView.as_view()),
    path('', items, name='items'),
    path('item/<pk>', items_detail, name='items'),
    path('buy/<pk>', ItemStripeAPIView.as_view())
]
