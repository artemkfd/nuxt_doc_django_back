from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework import routers
from django.views.static import serve
from .views import DocumentViewSet, DocumentList, DocumentDetail, documentDetail, create_document, DocFileViewSet

router = routers.DefaultRouter()
router.register(r'files', DocFileViewSet)
router.register(r'docs', DocumentViewSet)


# Привязываем наше API используя автоматическую маршрутизацию.
# Также мы подключим возможность авторизоваться в браузерной версии API.
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^create_document/(?P<pk>[0-9]+)/$', create_document),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^doc_detail/(?P<pk>[0-9]+)/$', documentDetail),

    path('schema/', schema_view),
    path('api-auth/', include('rest_framework.urls')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
