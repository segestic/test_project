from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.decorators import student_only
from django.http import HttpResponse
from .models import Mail
from django.http import HttpResponseRedirect
from .models import Mail
from .forms import MailForm, SendMailForm
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    user = request.user
    total_messages = Mail.objects.filter(user_id=user.id)#.all()
    unread_messages = total_messages.filter(is_read=False)
    context = {
        'total_messages':total_messages.count(),
        'unread_messages':unread_messages.count(),

    }
    return render(request, 'inbox/status.html', context)

from django.views import generic

class MailDetailView(generic.DetailView):
    form_class = MailForm
    template_name = 'inbox/mail_detail.html' 
    pk_url_kwarg = "pk"  

    def get_queryset(self, *args, **kwargs):
        user_messages = Mail.objects.filter(user=self.request.user).all()
        specific = user_messages.filter(id=self.kwargs['pk'])
        specific.update(is_read=True)
        return specific 


class MailCreateView(generic.CreateView):
    model = Mail
    form_class = SendMailForm
    #success_message = 'Message successfully sent!!'
    template_name = 'inbox/mail_create_form.html'

    def form_valid(self, form):
        mail = form.save()
        messages.success(self.request, "Message successfully sent!!")
        return redirect('mail_create')
    

class MailListView(generic.ListView):
    # model = Mail
    # queryset = Mail.objects.all().order_by('-id')
    context_object_name = 'mail'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        user_messages = Mail.objects.filter(user=self.request.user).all().order_by('-id')
        return user_messages 
