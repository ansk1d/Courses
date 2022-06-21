from django.urls import path     
from . import views
urlpatterns = [
    path('', views.showcourse),
    path('addcourse', views.addcourse),
    path('rusure/<_id>',views.delcourse),
    path('delete/<_id>', views.delete)
]