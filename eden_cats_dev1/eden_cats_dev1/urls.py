"""eden_cats_dev1 URL Configuration

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
from apps.blog import views
# from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('articles/<int:id>/', views.detail, name='detail'),
    path('category/<int:id>/', views.search_category, name='category_menu'),  # 分类搜索
    path('categories/', views.category_show, name='category_show'),  # 归类页
    path('tag/<str:tag>/', views.search_tag, name='search_tag'),  # 标签搜索
    path('tags/', views.tags_cloud, name='tags_cloud'),  # 标签
    path('archives/<str:year>/<str:month>', views.archives, name='archives'),  # 归档
    path('summernote/', include('django_summernote.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django jet urls
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET Dashboard URLS
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
