from django.urls import include, path

urlpatterns = [
    path('meter/', include('meter.urls')),
]