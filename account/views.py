from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, DataForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    message = ''
    if request.method == 'POST':
        data = DataForm(request.POST)
        try:
            data.save()
        except ValueError:
            message = 'Invalid entry'
        else:
            message = 'added successfully'

    form = DataForm()
    return render(request, 'account/index.html', {'form':form, 'message': message})

def register(request):
    if request.method == 'POST':
        # Get form data from the post
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form})
