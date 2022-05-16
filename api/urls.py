from django.urls import path, include
from django.urls import re_path
# from django.conf.urls import url
from .views import CustomerSignUpView, ObtainAuthTokenView, CustomConfirmEmailView
#from .import  views


urlpatterns = [
    #API URLS BEGINSSSSS
    # path('api-auth/', include('rest_framework.urls')), #for development
    path('rest-auth/', include('rest_auth.urls')), #must be on , has rest-login, logout.
    re_path('rest-auth/registration/account-confirm-email/(?P<key>.+)/', CustomConfirmEmailView.as_view(), name='account_confirm_email'), ##NEW 2022 for confirm email to work
    #Registration Urls
    path('registration/customer/', CustomerSignUpView.as_view(), name='register-customer'),
]


###############MESSAGES#########.

from django.urls import path
from . import views
urlpatterns += [
    path("inbox/",views.ListInboxAPIView.as_view(),name="inbox_list"),
    path("inbox/create/", views.CreateInboxAPIView.as_view(),name="inbox_create"),
    path("inbox/detail/<int:pk>/", views.DetailInboxAPIView.as_view(), name="inbox_detail"),
]


#from rest_framework.authtoken.views import obtain_auth_token  overwritten

urlpatterns += [
    path('api-token-auth2/', ObtainAuthTokenView.as_view(), name="api-token-auth2"), # 
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]



