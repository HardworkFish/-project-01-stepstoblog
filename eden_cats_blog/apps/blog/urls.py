"""eden_cats_blog URL Configuration

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
from django.contrib import admin
from django.urls import path
# from apps.blog import views
from django.conf.urls import url, include
from . import views

app_name = 'apps.blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('article/<int:id>/', views.detail, name='detail'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    path('category/<int:id>/', views.search_category, name='category_menu'),
    path('tag/<str:tag>/', views.search_tag, name='search_tag'),
    path('archives/<str:year>/<str:month>', views.archives, name='archives'),  # 按月归档
    # path('archives/<str:year>/<str:month>', views.archives, name='archives'),  # 按月归档
    path('articles/<int:id>/', views.detail, name='detail'),
    path('accounts/profile/', views.account_profile, name='account_profile'),
    path('accounts/', include('allauth.urls'))
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# url(r' ', include('eden_cats_dev1.urls')),
# ]
