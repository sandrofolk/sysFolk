"""sysfolk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
# from django.views.generic.base import RedirectView
from jet.dashboard.dashboard_modules import google_analytics_views
from rest_framework import routers

from sysfolk.authentication.views import MyUserViewSet
from sysfolk.core.views import home, PersonViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'user', MyUserViewSet)
router.register(r'person', PersonViewSet)
# routeCore.register(r'user', UserViewSet)


urlpatterns = i18n_patterns(
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    # url para autenticação
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # controle de usuario no navegador
    url(r'^rest-auth/', include('rest_auth.urls')),

    url(r'^$', home, name='home'),
    url(_(r'^admin/'), admin.site.urls),
    url(_(r'^api/'), include(router.urls)),
    # url(r'^$', RedirectView.as_view(url='/admin')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
