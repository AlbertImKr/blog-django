from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
                  path("accounts/", include("accounts.urls")),
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
