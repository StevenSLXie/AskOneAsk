from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^login', 'django.contrib.auth.views.login', {'template_name':'/Users/xingmanjie/Applications/Python/AskAndAnswer/askandanswer/lists/templates/login.html'},name='login'),
	url(r'^$','lists.views.print_answers',name='print answers'),  #signup
	url(r'^ask','lists.views.new_ask',name='new ask'),
	url(r'^answer','lists.views.new_answer',name='new answer'),
    # url(r'^blog/', include('blog.urls')),

	#url(r'^admin/', include(admin.site.urls)),
)
