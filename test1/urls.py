from django.urls import path

from . import views

urlpatterns=[
    path("ht",views.index,name="index"),
    path("lvpeisong",views.lvpeisong,name="lvpeisong"),
    path("chenyiming",views.chenyiming,name="chenyiming"),
    path("liuhangdong",views.liuhangdong,name="liuhangdong"),
    path("jiayawei",views.jiayawei,name="jiayawei"),
    path("leiyaxi",views.leiyaxi,name="leiyaxi"),
    path('otboys/insert',views.create_otboys,name='insert_otboys_info'),
    path('otboys/toinsert',views.tocreate,name='tocreate_otboys'),
]