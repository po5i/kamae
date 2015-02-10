from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^signin/', signin, name='signin'),
    url(r'^signout/', signout, name='signout'),
    url(r'^mark/', mark, name='mark'),
    url(r'^do_mark/', do_mark, name='do_mark'),
    url(r'^kenshi/', kenshi, name='kenshi'),
    url(r'^new_kenshi/', new_kenshi, name='new_kenshi'),
    url(r'^names/', names, name='names'),
)