from django.contrib import admin
from django.urls import path, include # 确保 include 已导入
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar # 确保导入

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('comments/', include('comments.urls')),
    path('foodie/', include('foodie.urls', namespace='foodie')),
    path('accounts/', include('accounts.urls')),  # 添加 accounts 应用的URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))] # Django Debug Toolbar