from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static


from blogs.views import custom_404_view, home


urlpatterns = [
    path('blog-admin/', admin.site.urls),
    path('home/', include('blogs.urls')),
    path('', home),
    re_path(r"^", custom_404_view),
    path('froala_editor/', include('froala_editor.urls')),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


