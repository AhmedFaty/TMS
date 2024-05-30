from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request," ")
            return redirect("live:tache_list")
        else:
            messages.success(request, "There was an error, please try again...")
            return render(request, "accounts/login.html", {})


    else:
        return render(request, "accounts/login.html", {})



def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return render(request, "accounts/login.html", {})


class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = "accounts/edit_profil.html"
    success_url = reverse_lazy("accounts")

    def get_object(self):
        return self.request.user
    

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect("accounts:password_change_done")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change_form.html', {'form': form})
