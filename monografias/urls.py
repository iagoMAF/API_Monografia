from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
import rest_framework.permissions as permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Api monografias",
        default_version='v1',
        description="Api de acesso ao sistema de registro de monografias - SD2024/1",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=(JWTAuthentication,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('equipe.urls')), 
    path('', include('historico.urls')),
    #path('/', include('documentos.urls')),   # Mantém a rota pdfs/ funcional
    path('', include('documentos.urls')),
    path('', include('usuarios.urls')), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
