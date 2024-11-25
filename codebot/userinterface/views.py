from django.shortcuts import render, redirect
from django.contrib import messages
from .utils.helper import languages, codecorrect, codegen
from django.contrib.auth import authenticate, login, logout
from . form import SignUpForm
from .models import Code

def home(request):
    lang_list = languages()
    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']
        if lang == 'Select Language':
            messages.success(request, "You forget to pick a Language")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        else:
            try:
                respons = codecorrect(code, lang)
                code_save = Code(user=request.user,question=code, answer=respons, language=lang)
                code_save.save()
                return render(request, 'home.html', {'lang_list': lang_list, 'respons': respons, 'lang': lang})
            except Exception as e:
                return render(request, 'home.html', {'lang_list': lang_list, 'respons': e, 'lang': lang})
            
    return render(request, 'home.html', {'lang_list': lang_list})

def suggest(request):
    lang_list = languages()
    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']
        if lang == 'Select Language':
            messages.success(request, "You forget to pick a Language")
            return render(request, 'suggest.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        else:
            try:
                respons = codegen(code)
                code_save = Code(user=request.user,question=code, answer=respons, language=lang)
                code_save.save()
                return render(request, 'suggest.html', {'lang_list': lang_list, 'respons': respons, 'lang': lang})
            except Exception as e:
                return render(request, 'suggest.html', {'lang_list': lang_list, 'respons': e, 'lang': lang})
            
    return render(request, 'suggest.html', {'lang_list': lang_list})

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password =  form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Sign Up Successful!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'signup': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user =  authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return redirect('login')
    
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been Logged Out')
    return redirect('home')

def history(request):
    if request.user.is_authenticated:
        codes = Code.objects.filter(user_id=request.user.id)
        return render(request, 'code.html', {'past_code':codes})
    else:
        messages.success(request, 'You are not Loggedin')
        return redirect('home')

def delete(request, code_id):
    del_code = Code.objects.get(pk=code_id)
    del_code.delete()
    messages.success(request, 'Code block is deleted ... ')
    return redirect('history')

def about(request):
    return render(request, 'about.html', {})