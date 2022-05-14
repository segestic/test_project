from ast import Is
# Create your views here.
from django.shortcuts import render
from accounts.models import Customer

# Create your views here.

#from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    CustomerSignUpSerializer,  MyLoginSerializer
    )

class CustomerSignUpView(RegisterView):
    serializer_class = CustomerSignUpSerializer
    queryset = Customer.objects.all().order_by('-user_id') 
    permission_classes = (AllowAny,)#allowing anyone to register here and overiding the only authenticated permission in settings.py (project level)
                                    #note using tuple (AllowAny) here instead of dictionary [AllowAny] for security, same should be for urls, settings etc.

    


from rest_framework.views import APIView    
from .custom_permissions import IsCustomer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

class HelloTestView(APIView):
    def get(self, request):
        context = {"message": "Hello, World!"} # <------ Response to the client
        return Response(context)




from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class ObtainAuthTokenView(APIView):
    serializer_class = MyLoginSerializer
    permission_classes = [IsAuthenticated & (IsCustomer)]

    def post(self, request):
        context = {}

        username = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(username=username, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfull.'
            #context['pk'] = account.pk #i dont need to tell them their pk
            context['username'] = username
            context['token'] = token.key
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'

        return Response(context)

#documentation



################--TODO---------
from rest_framework import viewsets
from .serializers import MailSerializer
from inbox.models import Mail


    
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

    
class ListInboxAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = [IsAuthenticated & (IsCustomer)]
    queryset = Mail.objects.all().order_by('-created')
    serializer_class = MailSerializer
    
class CreateInboxAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    permission_classes = [IsAuthenticated & (IsCustomer)]
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    
class UpdateInboxAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    permission_classes = [IsAuthenticated & (IsCustomer)]
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    
class DeleteInboxAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    permission_classes = [IsAuthenticated & (IsCustomer)]
    queryset = Mail.objects.all()
    serializer_class = MailSerializer    