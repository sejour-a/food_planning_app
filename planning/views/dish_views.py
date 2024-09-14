from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from planning.models import Dish
from planning.serializers import DishSerializer


class Dishes(APIView):
    serializer_class = DishSerializer

    def get(self, _):
        dishes = Dish.objects.all()
        serialized_dishes = DishSerializer(dishes, many=True)
        return Response(serialized_dishes.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = DishSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DishDetail(APIView):
    serializer_class = DishSerializer

    def get_object(self, pk):
        try:
            return Dish.objects.get(pk=pk)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, _, pk):
        dish = self.get_object(pk)
        serialized_dish = DishSerializer(dish)
        return Response(serialized_dish.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        dish = self.get_object(pk)
        serialized_dish = DishSerializer(dish, data=request.data)
        if serialized_dish.is_valid():
            serialized_dish.save()
            return Response(serialized_dish.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_dish.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        dish = self.get_object(pk)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
