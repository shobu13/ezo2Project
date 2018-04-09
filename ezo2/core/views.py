"""Module servant à afficher les pages composant l'application Core."""
from django.shortcuts import render, redirect, reverse
import global_var
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from core.forms import CreateUserForm, ConnexionForm
from core.models import Profil


def home(request):
    """affiche la page d'acceuil du core"""
    return render(request, 'core/home.html', {'global': global_var})


def a_propos(request):
    """vue affichant diverse informations sur la communauté et ses membres."""
    return render(request, 'core/aPropos.html', {'global': global_var})


def connexion(request):
    """vue affichant la page de connexion et traitant les données de cette dernière."""
    msg = ''
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'core/home.html', {'global': global_var, 'connexion': True})
            else:
                msg = "Mot de passe ou nom d'utilisateur inconnu"
    else:
        form = ConnexionForm()

    return render(request, "core/connexion.html", {'global': global_var, 'msg': msg,
                                                   'form': form})


def afficher_profil(request):
    """affiche le profil de l'utilisateur connecté et permet sa mofification"""
    if request.method == "POST":
        description = request.POST['description']
        user = request.user
        try:
            user.profil.description = description
            user.profil.save()
        except:
            profil = Profil(user=user, description=description)
            profil.save()

    return render(request, "core/afficherProfil.html", {'global': global_var, })


def deconnexion(request):
    """vue permetant à l'utilisateur de se déconnecter, renvoie vers la page d'acceuil avec la
    variable déconexion à True pour afficher une popup"""
    logout(request)
    return render(request, 'core/home.html', {'global': global_var, 'deconnexion': True})


def inscription(request):
    """vue affichant la page d'inscription et traitant les données de cette dernière."""
    msg = ''
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = request.POST["confirm-password"]
            if password == confirm_password:
                form.save()
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                msg = 'utilisateur créer'
            else:
                msg = 'les deux mot de passe ne correspondent pas.'
        else:
            msg = 'le formulaire est invalide.'
    else:
        form = CreateUserForm()
    return render(request, "core/inscription.html", {'global': global_var, 'form': form,
                                                     'msg': msg})

