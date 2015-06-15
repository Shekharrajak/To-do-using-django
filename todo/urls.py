from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/(.*)',admin.site.root),
    url(r'^$','todo.core.view.index'),
)
