from ast import Is
# Create your views here.
from django.shortcuts import render
from accounts.models import User, Customer
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

    



##########################
from rest_framework.views import APIView    
from .custom_permissions import IsCustomer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
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



################--INBOX---------
from rest_framework import viewsets
from .serializers import MailSerializer, CreateMailSerializer
from inbox.models import Mail


    
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView



class ListInboxAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = [IsAuthenticated & (IsCustomer)]
    authentication_classes = (TokenAuthentication,)
    serializer_class = MailSerializer
    # queryset = Mail.objects.all().order_by('-created')

    def get_queryset(self, *args, **kwargs): 
        try:
        # user_messages = Mail.objects.filter(user=self.request.user).all().order_by('-id')
            user_messages = Mail.objects.filter(user=self.request.user).only('subject', 'content', 'is_read').order_by('-id')
        except:
            return Response('errors', status=400)             
        return user_messages 


class DetailInboxAPIView(APIView):
    http_method_names = ['get', 'head']
    permission_classes = [IsAuthenticated & (IsCustomer)]
    authentication_classes = (TokenAuthentication,)
    # queryset = Mail.objects.all().order_by('-created')
    serializer_class = MailSerializer 
    
    def get(self, *args, **kwargs):
        try:
            user_messages = Mail.objects.filter(user=self.request.user).all()
            specific = user_messages.filter(id=self.kwargs['pk'])
            specific.update(is_read=True)
            data = MailSerializer(specific[0]).data##Must_be_sliced
        except:
            return Response('input errors', status=400) 
        return Response(data, status=200) 
 

#to use username instead of user_id    
class CreateInboxAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    permission_classes = [IsAuthenticated & (IsCustomer)]
    authentication_classes = (TokenAuthentication,)
    # queryset = Mail.objects.all()
    serializer_class = CreateMailSerializer

    def post(self, request, *args, **kwargs):
        recipent =  request.data.get("recipent_username")            
        if not recipent:
            return Response('recipent_username is required', 400)
        subject = request.data.get("subject")
        content = request.data.get("content")
        try:
            user_id = User.objects.get(username=recipent).id
        except:    
            return Response('errors', 400)
        data = {'subject': subject, 'content': content, 'user_id': user_id}
        serializer = CreateMailSerializer(data=data)
        # return Response(serializer.data)
        if serializer.is_valid():
            new = Mail.objects.create(subject=subject, content=content, user_id=user_id)
            new.save()
            return Response({
            'status': 'successfully created',
            'subject': str(new.subject),
            'content': str(new.content),
            'recipent': recipent,
        }, status=201)
            # return Response('Successfully Created', 201)
        else:
            return Response(serializer.errors, 400)



# class CreateInboxAPIView(CreateAPIView):
#     """This endpoint allows for creation of a todo"""
#     permission_classes = [IsAuthenticated & (IsCustomer)]
#     authentication_classes = (TokenAuthentication,)
#     # queryset = Mail.objects.all()
#     serializer_class = CreateMailSerializer

#     def post(self, request, *args, **kwargs):
#         try:
#             subject = request.data.get("subject")
#             content = request.data.get("content")
#             user_id =  request.data.get("user_id")
#             data = {'subject': subject, 'content': content, 'user_id': user_id}
#             serializer = CreateMailSerializer(data=data)
#             if serializer.is_valid():
#                 new = Mail.objects.create(subject=subject, content=content, user_id=user_id)
#                 new.save()
#                 return Response({
#                     'status': 'successfully created',
#                     'subject': str(new.subject),
#                     'content': str(new.content),
#                     'recipent': user_id,
#                 }, status=201)
#             else:
#                 return Response(serializer.errors, 400)
#         except:
#             return Response('input errors', status=400) 



######FOR django-rest-auth activate email to work.

from allauth.account.views import ConfirmEmailView
from django.contrib.auth import get_user_model
#seg
from allauth.account.models import EmailAddress
from django.shortcuts import redirect
from django.contrib.auth import login
from django.http import Http404

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
        user = get_user_model().objects.get(email=self.object.email_address.email)
        verify = EmailAddress.objects.get(user_id=user.id) #filter has no attribute save. its only get - specific queryset that has attribute save..
        verify.verified = True
        verify.save() 
        # messages.success(self.request, ('Your email have been verified.'))
        login(self.request, user)
        redirect_url = '/'  #reverse('user', args=(user.id,))
        return redirect(redirect_url)




##################

