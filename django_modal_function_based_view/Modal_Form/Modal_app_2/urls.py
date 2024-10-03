from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='App_home'),
    path('add', views.add_record, name='app_addrecord'),
    path('update<int:id>',views.update_record,name='app_update'),
    path('delete<int:id>',views.delete_record ,name='app_delete'),
]
