from django.urls import path
from .import  views

urlpatterns=[
    path('', views.index, name='dashboard-index'),

    path("list/", views.MailListView.as_view(), name="mail_list"),
    path("create/", views.MailCreateView.as_view(), name="mail_create"),
    path("detail/<int:pk>/", views.MailDetailView.as_view(), name="mail_detail"),
    # path("update/<int:pk>/", views.StyleUpdateView.as_view(), name="style_update"),
    #  path('',views.login_request, name='login'),
    #  path('login/',views.login_request, name='login'),
    #  path('logout/',views.logout_view, name='logout'),
]