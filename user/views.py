from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def registration(request):
    
    if request.method == 'POST':
        
        
        u_name = request.POST['name']
        u_email = request.POST['Email']
        u_password = request.POST['password'] 

        user = User.objects.create_user(username= u_name, email = u_email , password = u_password)
        user.save();
        
        return redirect ('/') 
    
    else:
        return render(request, 'user_login.html') 
        


##other process
# def add_user(request):

#     user_name = request.POST['name']
#     user_email = request.POST['Email']
#     user_pass = request.POST['password']       
#     print(user_name)
#     print(user_email)
#     print(user_pass)
#     user = User.objects.create_user(username=user_name, password = user_pass , email = user_email)
#     user.save();

#     return redirect('/')