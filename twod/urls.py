from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('foodie/', include('foodie.urls', namespace='foodie')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()
