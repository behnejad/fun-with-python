from django.conf.urls import include, url
from django.contrib import admin
from contact.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'contact.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('getList$', getList, name="getList"),
    url('addPerson$', addPerson, name="addPerson"),
    url('rmPerson$', delPerson, name="rmPerson"),
    url('updatePerson$', update, name="updatePerson"),
]
