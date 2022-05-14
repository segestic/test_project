from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework.authtoken.models import Token

#from accounts.models import Seller, Buyer      

#custom login serializer for the purpose of removeing the username field

class MyLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username"""

    email = None        
    
    
################
from django.db import transaction
from accounts.models import User,Customer
from rest_framework.validators import UniqueValidator

CUSTOMER = 1



# user_type = forms.ChoiceField(choices=USER_CHOICES, required=True, widget=forms.RadioSelect)

class CustomerSignUpSerializer(RegisterSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,)
    first_name = serializers.CharField(required=True,)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Customer.objects.only('phone_number'))])
    location = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
        data = super(CustomerSignUpSerializer, self).get_cleaned_data()
        extra_data = {
            'first_name' : self.validated_data.get('first_name', ''),
            'last_name' : self.validated_data.get('last_name', ''),
            'email' : self.validated_data.get('email', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'location': self.validated_data.get('location', ''),
        }
        data.update(extra_data)
        return data

    @transaction.atomic
    def save(self, request):
        user = super(CustomerSignUpSerializer, self).save(request)
        user.user_type = 1
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        #user.is_active = True #all-auth and rest-auth automatically makes all accounts active        
        user.email = self.cleaned_data.get('email')
        #first save the initial data
        #user.user_type = 1
        user.save()
        patient = Customer.objects.create(user=user)
        patient.phone_number=self.cleaned_data.get('phone_number')
        patient.location=self.cleaned_data.get('location')
        patient.blood_group = self.cleaned_data.get('blood_group')
        patient.save()
        return user


    

###############--MAIL BEGINS HERE -------------        



from inbox.models import Mail

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"
        