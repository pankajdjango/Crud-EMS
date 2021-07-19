from django.urls import path
from .views import index,update,delete
urlpatterns = [
    path('',index,name='home'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
]
