
from django.urls import path
from .views import lead_list, lead_detail, lead_create

app_name = "leads"

urlpatterns = [ #Personalized url's example: '/leads/
    path('', lead_list),
    path('<int:pk>/', lead_detail),
    path('create/', lead_create)
]