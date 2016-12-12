from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^Bike/$', 'Bike.views.index'),
    url(r'^Bike/signup/$','Bike.views.signup'),
    url(r'^Bike/signin/$','Bike.views.signin'),
    url(r'^Bike/signout/$','Bike.views.signout'),
    url(r'^Bike/person/$','Bike.views.person'),
    url(r'^Bike/rentbike/$','Bike.views.rentbike'),
    url(r'^Bike/returnbike/$','Bike.views.returnbike'),
    
)
