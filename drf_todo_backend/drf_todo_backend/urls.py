from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views


API_TITLE = 'Todo API'
API_DESCRIPTION = 'A Web API for creating and viewing Todo List.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False), name=''),
    path('admin/', admin.site.urls),

    path('api/', include('todo.urls'), name='api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),

    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
