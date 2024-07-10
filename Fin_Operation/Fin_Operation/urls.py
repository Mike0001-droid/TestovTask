from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from api.views import BankAccountViewSet, TransactionsViewSet
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'accounts', BankAccountViewSet, basename='accounts')
router.register(r'transactions', TransactionsViewSet, basename='transactions')

urlpatterns = [
    path('docs/', include(router.urls)),
    path('api/', include_docs_urls(title='API docs')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)