# askandanswer/tables.py
import django_tables2 as tables
from lists.models import Qns,Ans,Person
#from lists.views import people_detail
from django_tables2.utils import A
from django.contrib.auth.models import User



# the table displays the questions that the current user have asked.
class QnsTable(tables.Table):
    '''
    class Meta:
        model = Ans
        fields = ('getQns','answer','person',)
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
    '''
    getQns = tables.Column(accessor='getQns')
    answer = tables.Column(accessor='answer')
    person = tables.LinkColumn('people_detail',args=[A('person')])
    attrs = {'class':'paleblue'}

# the table displays the questions that the current use have answered.		
class AnsTable(tables.Table):
    '''
    class Meta:
        model = Ans
        fields = ('getQns','askedByWhom','answer',)
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
    '''
    getQns = tables.Column(accessor='getQns')
    askedByWhom = tables.LinkColumn('people_detail',args=[A('askedByWhom')])
    answer = tables.Column(accessor='answer')
    attrs = {'class':'palablue'}

# the table display the user info.
class UserTable(tables.Table):
    class Meta:
        model = Person 
        fields = ('get_username','email','city','status')
        attrs = {'class':'paleblue'}
