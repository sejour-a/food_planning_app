from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),

    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('api/groceries/', include("groceries.urls")),
    path('api/planning/', include("planning.urls")),
]
