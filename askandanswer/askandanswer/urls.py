from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^login', 'django.contrib.auth.views.login', {'template_name':'/Users/xingmanjie/Applications/Python/AskAndAnswer/askandanswer/lists/templates/login.html'},name='login'),
	url(r'^signup','lists.views.signup',name='sign up'),
	url(r'^$','lists.views.home',name='home'),
	url(r'^ask','lists.views.new_ask',name='new ask'),
	url(r'^answer','lists.views.new_answer',name='new answer'),
	url(r'^myqns','lists.views.print_qns_by_asker',name = 'view my qns'),
	url(r'^myans','lists.views.print_answer_by_answerer',name = 'view my answer'),
	url(r'^people','lists.views.people_detail',name='people_detail'),
    # url(r'^blog/', include('blog.urls')),

	#url(r'^admin/', include(admin.site.urls)),
)
