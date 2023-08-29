from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .helpers import send_forget_password_mail
from .forms import addForm
import pandas as pd

# Create your views here.

#@login_required
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    keys = s_data.objects.filter(key__icontains=q)
    context = {'keys':keys}
    return render(request , 'home.html', context)



def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')


def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )










def Logout(request):
    logout(request)
    return redirect('/')




def ChangePassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/accounts/login')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'change-password.html' , context)


def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget-password.html')



def browse(request):
    scholarships = s_data.objects.all()
    return render(request , 'browse.html' , {"scholarships":scholarships})

def information(request , pk):

    scholarship = None
    scholarship = s_data.objects.get(id=pk)
    return render(request, 'information.html' , {'scholarship':scholarship})


@login_required
def addScholarship(request):

    scholarships = Scholarship.objects.all()
    form = addForm()
    if request.method == 'POST':
        form = addForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            field = data['name']
            print(field)
            form.save()
            return redirect('home')
    context = {'form' : form}

    return render(request, 'addScholarship.html' , context)


''' import joblib
from joblib import load
#myfile = load('./savedModels/model.joblib')

from nbimporter import NotebookLoader
import os
# Load the notebook containing the function
notebook_path = ('./notebooks/test.ipynb')
loader = NotebookLoader()
my_notebook = loader.load_module(notebook_path)
print(notebook_path) '''

import pickle
import pandas as pd

def recommender(request):
    if request.method == 'POST':
        Key = request.POST.get('Key', False)
        Level = request.POST.get('Level', False)
        Language = request.POST.get('Language', False)
        Accomodation_covered = request.POST.get('Accomodation covered?')
        Living_Expense_Covered = request.POST.get('Living Expense Covered?')



        data = ([[Key, Level, Language, Accomodation_covered, Living_Expense_Covered]])
        print(data)

        with open('savedModels\processed_df.pkl', 'rb') as f:
            ohe1 = pickle.load(f)
            ohe2 = pickle.load(f)
            LogReg = pickle.load(f)

        #result = myfile.predictor(data)
        # Call the function defined in the notebook
        data = pd.DataFrame(data, columns=['Key', 'Level', 'Language', 'Accomodation covered?', 'Living Expense Covered?'])
        data1 = ohe1.transform(data[['Key']])
        data2 = ohe2.transform(data[['Level','Language','Accomodation covered?','Living Expense Covered?']])
        data1 = pd.DataFrame(
            data1, 
            columns=ohe1.get_feature_names_out()
        )

        data2 = pd.DataFrame(
            data2, 
            columns=ohe2.get_feature_names_out()
        )
        data = pd.concat([data1, data2], axis = 1)
        prediction = LogReg.predict(data)
        print(prediction[0])

        return render(request, 'recommender.html', {'result' : prediction[0]})
    return render(request, 'recommender.html') 


