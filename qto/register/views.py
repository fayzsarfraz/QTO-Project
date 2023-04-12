from django.shortcuts import render

# import Httpresponse to use function  cls

from django.shortcuts import HttpResponse
# import redorect  to use redirect fun
from django.shortcuts import redirect
# Once you have imported the User model, you can use it to create, retrieve, update, 
# or delete user accounts in your Django application. The User model provides fields such as username, 
# email, password, and first_name/last_name that you can use to store user information. You can also 
# extend the User model by creating a custom user model that inherits from AbstractUser or
# AbstractBaseUser, depending on your requirements.

# Note that in newer versions of Django (2.2+), it is recommended to use a custom user model instead of
# the built-in User model, as it provides more flexibility and customization options.
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    # return render(request,'index.html')
      if request.method=='POST':
            uname=request.POST.get('FirstName')
            ulname=request.POST.get('LastName')
            uemail=request.POST.get('uemail')
            upass1=request.POST.get('Password1')
            upass2=request.POST.get('Password2')
            # print(uname,ulname,uemail,upass1,upass2)
            my_user=User.objects.create_user(uname,uemail,upass1)
            my_user.save()
            # return redirect('login/index.html')
      return render(request, 'register/index.html')