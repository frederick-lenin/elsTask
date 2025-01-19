from django.shortcuts import render, redirect
from .models import Admin,Student,Role
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.decorators import api_view
# from django.contrib.auth.hashers import check_passwordtoken
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # email = request.POST.get('email')
        # phone = request.POST.get('phone')
        # password =request.POST.get('password')
        roleid =request.POST.get('roleid')
        
        if Admin.objects.filter(roleid=roleid).exists():
            return HttpResponse(f"Error: A member with the {roleid} already exists.")
        
        # Create and save the new member
        admin_cre = Admin(name=name,roleid=roleid)
        admin_cre.save()

        # Redirect or return a response
        return HttpResponse(f" {name} added successfully!")

    return render(request, 'myapp/add_member')

@csrf_exempt
@api_view(['POST'])
def role_create(request):
    # if request.method =='POST':
    name=request.POST.get('name')
    
    if Role.objects.filter(name=name).exists():
        return HttpResponse(f" {name} already exists.")
        
    new_role=Role(name=name)
    new_role.save()
    
    return HttpResponse(f"{name} added sucessfully")
    
    
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password =request.POST.get('password')
        role_name=request.POST.get('role')
        print("rollname",role_name)
        role = Role.objects.filter(id=role_name).first() 
        
        # if not role:
        #     return HttpResponse(f"Error: Role '{role_name}' does not exist.")
        # print(role)
        # return HttpResponse("succcss")
      
        if Student.objects.filter(email=email).exists():
            return HttpResponse(f"correct details already exists")
        student = Student(name=name,email=email,password=password,Role=role)
        student.save()
        user = LoginSerializer(Student)
        Refresh = RefreshToken.for_user(user)
        acess =Refresh.access_token
        return Response({
            "data": "data created sucessfully",
            "acess": acess,
            "refresh": Refresh
            
        },status= status.HTTP_201_CREATED)
                        

        
    
    
    
    
    
    

