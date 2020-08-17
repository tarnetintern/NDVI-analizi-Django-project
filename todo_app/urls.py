from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('merhaba', views.index),
    path("hakkinda",views.deneme,name="hakkinda"),
    path("",views.anaSayfa,name="anaSayfa"),
    path("ndviolustur",views.ndviolustur,name="ndviolustur"),
    path("ndvihesaplama",views.ndvihesaplama,name="ndvihesaplama"),
    path("mainpage",views.main)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)