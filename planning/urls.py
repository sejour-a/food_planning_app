from django.urls import path

from planning.views import (
    Days,
    DayDetail,

    Dishes,
    DishDetail,

    Weeks,
    WeekDetail,
)


app_name = 'groceries'


urlpatterns = [
    path('days/', Days.as_view()),
    path('days/<int:pk>', DayDetail.as_view()),

    path('dishes/', Dishes.as_view()),
    path('dishes/<int:pk>', DishDetail.as_view()),

    path('weeks/', Weeks.as_view()),
    path('weeks/<int:pk>', WeekDetail.as_view())
]