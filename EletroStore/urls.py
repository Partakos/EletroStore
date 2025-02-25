from django.contrib import admin
from django.urls import path
from eletronicos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_produtos, name='lista_produtos'),
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
]

# Configuração para servir arquivos de mídia no modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
