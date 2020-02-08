from django.shortcuts import render
from django import forms

# Create your views here.
class UserLoginForm(forms.Form):
    """Form to login user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
def login(request):
    """Returns the login page"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST) 
        
        # populate the form from what the user has keyed in
        
        if login_form.is_valid():
            # attempt to check the username and password is valid
           
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in")
            if user:
                # log in the user
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {
                  'form':login_form
                })

    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {
            'form':login_form
        })

# def logout(request):
#     auth.logout(request)
#     messages.success(request, "You have successfully been logged out")
#     return redirect(reverse('index'))