from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from groceries import SECTIONS_IN_SHOP
from groceries.models import Item
from groceries.serializers import ItemSerializer


class ShopSectionList(APIView):
    def get(self, _, _f=None):
        return Response(SECTIONS_IN_SHOP, status=status.HTTP_200_OK)


class Items(APIView):
    serializer_class = ItemSerializer

    def get(self, _):
        items = Item.objects.all()
        serialized_items = ItemSerializer(items, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = ItemSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    serializer_class = ItemSerializer

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, _, pk):
        item = self.get_object(pk)
        serialized_item = ItemSerializer(item)
        return Response(serialized_item.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        item = self.get_object(pk)
        serialized_item = ItemSerializer(item, data=request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)