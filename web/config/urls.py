"""manifest URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView

from ksupcapp.core import views as core_views

admin.autodiscover()

urlpatterns = []

# Debug Toolbar
if settings.DEBUG:
    import debug_toolbar
    from django.contrib.staticfiles import views as staticviews
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^static/(?P<path>.*)$', staticviews.serve),
    ]

#from django.http import HttpResponse
#def out(a):
#    return HttpResponse(settings.PROJECT_DIR)
#urlpatterns += [url(r'^asdf$', out)]

# Normal URL Definition
urlpatterns += [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', core_views.home, name='home'),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^admin/', admin.site.urls),
]
