from django.urls import path, include
# from django.conf.urls import url
from .views import CustomerSignUpView, HelloTestView, ObtainAuthTokenView
#from .import  views


urlpatterns = [
    #API URLS BEGINSSSSS
    #Registration Urls
    path('registration/customer/', CustomerSignUpView.as_view(), name='register-customer'),
    path('test-api-view/', HelloTestView.as_view(), name='demo')
    #API URLS END, VIEWS START
]

#the namesppace specified in project level urls makes us to use app_name


from django.views.generic import TemplateView

#python manage.py runserver 5050

###############TODO.......

from django.urls import path
from . import views
urlpatterns += [
    path("v1/inbox/",views.ListInboxAPIView.as_view(),name="todo_list"),
    path("v1/inbox/create/", views.CreateInboxAPIView.as_view(),name="todo_create"),
    path("v1/inbox/update/<int:pk>/",views.UpdateInboxAPIView.as_view(),name="update_todo"),
    path("v1/inbox/delete/<int:pk>/",views.DeleteInboxAPIView.as_view(),name="delete_todo")
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



