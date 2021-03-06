"""ezo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog import views       # on importe le module contenant nos vues
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    # page d'acceuil (index)
    path('blog', views.home, name='blogHome'),
    # #formulaire de contact
    # path('contact', views.contact, name='contact'),
    # #page 404
    # path('404', views.e404, name='404'),
    # #formulaire d'ajout d'article
    # path('blog/addArticle', views.article, name='article'),
    path('blog/article/<int:id_article>-<slug:slug>', views.lire, name='lire'),
    path('blog/article_liste', views.article_liste, name='article_liste'),
    path('blog/article_liste/<int:page>/<str:keywords>/<str:selected_cat>', views.article_liste,
         name='article_liste'),
]

urlpatterns += staticfiles_urlpatterns()