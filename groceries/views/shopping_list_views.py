from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from groceries.models import ShoppingList
from groceries.serializers import ShoppingListSerializer


class ShoppingLists(APIView):
    serializer_class = ShoppingListSerializer

    def get(self, _):
        shopping_list = ShoppingList.objects.all()
        serialized_lists = ShoppingListSerializer(shopping_list, many=True)
        return Response(serialized_lists.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = ShoppingListSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ShoppingListDetail(APIView):
    serializer_class = ShoppingListSerializer

    def get_object(self, pk):
        try:
            return ShoppingList.objects.get(pk=pk)
        except ShoppingList.DoesNotExist:
            raise Http404

    def get(self, _, pk):
        shopping_list = self.get_object(pk)
        serialized_list = ShoppingListSerializer(shopping_list)
        return Response(serialized_list.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        shopping_list = self.get_object(pk)
        serialized_list = ShoppingListSerializer(shopping_list, data=request.data)
        if serialized_list.is_valid():
            serialized_list.save()
            return Response(serialized_list.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_list.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        shopping_list = self.get_object(pk)
        shopping_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)