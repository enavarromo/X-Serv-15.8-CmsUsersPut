from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^createPage/$', 'cms_put.views.createPage'),
    url(r'^mod/$', 'cms_put.views.managePages'),
    url(r'^accounts/profile/$', 'cms_put.views.redirectHome'),
    url(r'^login$','django.contrib.auth.views.login'),
    url(r'^logout$','django.contrib.auth.views.logout'),
    url(r'^$', 'cms_put.views.homePage'),
    url(r'(\d+)/', 'cms_put.views.pickPage'),
    url(r'^home/$', 'cms_put.views.homePage'),
    url(r'^admin/', include(admin.site.urls)),
)
