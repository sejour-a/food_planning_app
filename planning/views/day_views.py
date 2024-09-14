from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from planning.models import Day
from planning.serializers import DaySerializer


class Days(APIView):
    serializer_class = DaySerializer

    def get(self, _):
        days = Day.objects.all()
        serialized_days = DaySerializer(days, many=True)
        return Response(serialized_days.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = DaySerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DayDetail(APIView):
    serializer_class = DaySerializer

    def get_object(self, pk):
        try:
            return Day.objects.get(pk=pk)
        except Day.DoesNotExist:
            raise Http404

    def get(self, _, pk):
        day = self.get_object(pk)
        serialized_day = DaySerializer(day)
        return Response(serialized_day.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        day = self.get_object(pk)
        serialized_day = DaySerializer(day, data=request.data)
        if serialized_day.is_valid():
            serialized_day.save()
            return Response(serialized_day.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_day.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        day = self.get_object(pk)
        day.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)