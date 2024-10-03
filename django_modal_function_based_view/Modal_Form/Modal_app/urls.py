from django.urls import path
from.import views
urlpatterns =[
    path('', views.home, name='add'),
    path('add',views.add_record,name='app_addrecord'),
    path('update<int:ID>',views.update_record,name='app_update'),
    path('delete<int:ID>',views.delete_record ,name='app_delete'),
]
