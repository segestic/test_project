from django.urls import path, include
from django.urls import re_path
# from django.conf.urls import url
from .views import CustomerSignUpView, HelloTestView, ObtainAuthTokenView, CustomConfirmEmailView
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
    path("inbox/",views.ListInboxAPIView.as_view(),name="todo_list"),
    path("inbox/create/", views.CreateInboxAPIView.as_view(),name="todo_create"),
    path("inbox/update/<int:pk>/",views.UpdateInboxAPIView.as_view(),name="update_todo"),
    path("inbox/delete/<int:pk>/",views.DeleteInboxAPIView.as_view(),name="delete_todo")
]

#token - NEW
#from rest_framework.authtoken.views import obtain_auth_token  overwritten


urlpatterns += [
    path('api-token-auth2/', ObtainAuthTokenView.as_view(), name="api-token-auth2"), # 
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]








# from .api import TodoViewSet
# from rest_framework.routers import DefaultRouter
# #from django.urls import path, include



# ##################viewsets working but dont fully get how to call it....
# router = DefaultRouter()
# #router.register('', TodoViewSet, basename='todos')
# router.register('todos', TodoViewSet, basename='todos')
# #router.register("Room", views.RoomViewSet)
# #router.register("Hostel", views.HostelViewSet)
# #router.register("Course", views.CourseViewSet)
# #urlpatterns = router.urls#uncommnting this as i dont want to overide all urls


# urlpatterns += (
    # path("todo/", include(router.urls)), #api views

	# #....other... in case you have other urls #non-api views
    # #path("HMS/Student/", views.StudentListView.as_view(), name="HMS_Student_list"), #non-api views
# )



