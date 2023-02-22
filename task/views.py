from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.response import Response

from task.serializers import ItemModelSerializer
from task.models import Item
import stripe


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer

    @action(['GET'], detail=False)
    def success(self, request):
        return Response({"message": "Success!!!"})

    @action(['GET'], detail=False)
    def cancel(self, request):
        return Response({"message": "Cancel!!!"})


class ItemStripeAPIView(views.APIView):
    def get(self, request, pk=None):
        stripe.api_key = 'sk_test_26PHem9AhJZvU623DfE1x4sd'
        item = Item.objects.get(id=pk)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:4242/success',
            cancel_url='http://localhost:4242/cancel',
        )
        return Response({"session_id": session.id}, status=200)


def items(request):
    items = Item.objects.all()
    return render(request, 'item.html', context={'items': items})


def items_detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'index.html', context={'item': item})
