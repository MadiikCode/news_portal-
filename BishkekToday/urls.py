from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from news.views import news_list



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_list, name='home'),
    path('news/', include(('news.urls', 'news'), namespace='news')),
    path('users/', include("users.urls")),




    # path('admin/', admin.site.urls),
    # path('', include('news.urls')),
    # #path('news/', include(('news.urls', 'news'), namespace='news')),
    # path('users/', include("users.urls")),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
