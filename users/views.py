from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Two things are happening with this register function. We either generate a brand new form if it is a GET(else) request
# Or if the request is POST, we are taking the data the user entered and giving it to the form

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!') # This is a flash message to indicate the account is created
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})   # Left is a variable, right is what is instanced on line 5
