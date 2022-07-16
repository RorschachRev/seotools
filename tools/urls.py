from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tools.views.index', name='home'),
    url(r'^index.html', 'tools.views.index', name='home'),
    url(r'^keyword-vocab.html','tools.views.kw_vocab'),
    url(r'^backlinks.html','tools.views.bing_bl'),
    url(r'^pr_estimate.html','tools.views.pr_est'),
    
    url(r'^terms.html','tools.views.wn_lemma'),
    url(r'^term-dict.html','tools.views.wn_dict'),
    url(r'^term-verb.html','tools.views.verb_parse'),
    
    url(r'^verb/(?P<verb>[\w\-]+)/$', 'tools.views.verb'),
    url(r'^dict/(?P<term>[\w\-]+)/$', 'tools.views.wn_dict'),
    url(r'^term/(?P<term>[\w\-]+)/$', 'tools.views.wn_lemma'),
    url(r'^termj/(?P<term>[\w\-]+)/$', 'tools.views.term_js'),
    url(r'^termjson/(?P<term>[\w\-]+)/$', 'tools.views.term_json'),
)
