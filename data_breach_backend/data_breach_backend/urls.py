"""data_breach_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from rest_framework_nested import routers
from api.restful.viewset import DataBreachUploadViewset
from rest_framework.documentation import include_docs_urls


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'databreach', DataBreachUploadViewset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    re_path('^api/', include(router.urls)),
    re_path('^docs/', include_docs_urls(title='DATA BREACH APIs')),
    re_path(r'^', include('health_check.urls')),
]