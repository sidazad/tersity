from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'testserver.views.index', name='index'),
    url(r'^load_template','testserver.views.load_template',name='load_template'),
    url(r'^login_user','testserver.views.login_user',name='login_user'),
)
