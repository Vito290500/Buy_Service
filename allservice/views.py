from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse

from .models import User_Profile

# Create your views here.
class All_Service(View):
    def get(self, request):
        return render(request, "structure/all_service_page.html")

def Check_valid_user_input(self, user_input):
    
    message_validate_status = {}

    if  User_Profile.objects.filter(username=user_input['username']).exists():
        message_validate_status['user'] = "Username arleady exists."
    else:
        message_validate_status['user'] = "validate"

    if User_Profile.objects.filter(email=user_input['email']).exists():
        message_validate_status['email'] = "Email arleady exists."
    else:
        message_validate_status['email'] = 'validate'
      
    return message_validate_status
    
def Check_Password(request):
    user_data = request.session['user_input']

    if user_data['password'] == user_data['confirm_password']:
        return
    
    else:
        return render(request, "structure/register_page.html" ,{
                "message_not_validate" : "The password are not the same."
            })
    
def Email_validate(self, request, email):

    link_for_check= request.build_absolute_uri(reverse('confirm-email')) 

    subject = "Email Validation"
    message = f"Thanks for sign up!! \n please confirm email by clicking the following link {link_for_check}"
    from_email = "vitodivenosawork@gmail.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    request.session['email_to_validate'] = email

def ConfirmEmailAuthentication(request):

    new_user = User_Profile(
        username = request.session['user_input']['username'],
        email = request.session['user_input']['email'],
        password = request.session['user_input']['password'],
    )
    new_user.save()
    request.session.clear()

    return render(request, "structure/register_page.html" ,{
                "message_validate" : "Successfully Registered! Now you can Login."
            })
    
class RegisterPage(View):

    def get(self, request):
        return render(request, "structure/register_page.html")
    
    def post(self, request):
        user_input = request.POST

        if user_input['password'] != user_input['confirm_password']:
            return render(request, "structure/register_page.html" ,{
                "message_not_validate" : "The password are not the same."
            })

        request.session['user_input'] = user_input

        validate_status = Check_valid_user_input(self, user_input)

        if validate_status['user'] == 'validate' and validate_status['email'] == 'validate':
            
            Email_validate_status = Email_validate(self, request, request.POST['email'])

            return render(request, "structure/register_page.html",{
                "check_email_message" : "Check the email to complete the registration."
            })
    
        else:
            request.session.clear()

            if validate_status['user'] == "Username arleady exists.":

                return render(request, "structure/register_page.html",{
                    "message_not_validate" : "Username arleady exists."
                })
            
            else:
                 return render(request, "structure/register_page.html",{
                    "message_not_validate" : "Email arleady exists."
                })
            

class Login(View):
    
    def get(self, request):
        return render(request, "structure/login.html")
    
    def post(self, request):
        user_input = request.POST
        user_database = User_Profile.objects.filter(username = user_input['username'])

        if user_database.exists():
            get_data = User_Profile.objects.get(username= user_input['username'])

            if user_input['email'] != get_data.email:
                return render(request, "structure/login.html",{
                    "message": "Email wrong, please check the syntax or register."
                })
        
            elif user_input['password'] != user_database['password']:
                return render(request, "structure/login.html",{
                    "message": "Password wrong, please check the syntax."
                })
        
            else:
                return render(request, "structure/all_service_page.html",{
                    "profile_username" : user_input['username']
                })
            
            



        