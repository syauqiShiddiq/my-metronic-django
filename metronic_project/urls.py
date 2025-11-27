from django.contrib import admin
from django.urls import include, path

# --- TAMBAHAN PENTING 1 ---
from django.conf import settings
from django.conf.urls.static import static
# --------------------------

urlpatterns = [
    path('polls/', include('apps.polls.urls')),
    path('admin/', admin.site.urls),
]

# --- TAMBAHAN PENTING 2 ---
# Ini memaksa Django melayani file static saat mode DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
# --------------------------