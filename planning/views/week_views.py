from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from planning.models import Week
from planning.serializers import WeekSerializer


class Weeks(APIView):
    serializer_class = WeekSerializer

    def get(self, _):
        weeks = Week.objects.all()
        serialized_weeks = WeekSerializer(weeks, many=True)
        print(serialized_weeks.data)
        return Response(serialized_weeks.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = WeekSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class WeekDetail(APIView):
    serializer_class = WeekSerializer

    def get_object(self, pk):
        try:
            return Week.objects.get(pk=pk)
        except Week.DoesNotExist:
            raise Http404

    def get(self, _, pk):
        week = self.get_object(pk)
        serialized_week = WeekSerializer(week)
        return Response(serialized_week.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        week = self.get_object(pk)
        serialized_week = WeekSerializer(week, data=request.data)
        if serialized_week.is_valid():
            serialized_week.save()
            return Response(serialized_week.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_week.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        week = self.get_object(pk)
        week.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
