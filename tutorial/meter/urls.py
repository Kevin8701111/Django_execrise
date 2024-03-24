from django.urls import path
# from meter.meter_action import oneplusone
from meter import views

urlpatterns = [
    path('<str:address>/', views.Meter_AppReq.as_view(), name='meter_app_req'),
    # path('meter/<str:address>/', oneplusone.as_view()),
]