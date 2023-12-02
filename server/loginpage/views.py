# Create your views here.
from django.shortcuts import render, redirect
from .models import user_profile1
from django.contrib import messages

    
def register(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        username = request.POST['username']               
        email = request.POST['email']
        password = request.POST['password']
        
        if user_profile1.objects.filter(email=email).exists():
                messages.info(request, 'E-mail ID already exists!')
                return redirect('/signup')               
                
    
        elif user_profile1.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken!')
                return redirect('/signup')
                
        else:    
            x=user_profile1.objects.create(name=name,username=username,email=email,password=password)
            x.save()            
            print("User Created!")            
            return redirect('/login')       
            

    else:
        return render(request, 'registration.html')
    

def login(request):    
    return render(request, 'login.html')