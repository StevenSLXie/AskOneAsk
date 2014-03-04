# askandanswer/tables.py
import django_tables2 as tables
from lists.models import Qns,Ans


# the table displays the questions that the current user have asked.
class QnsTable(tables.Table):
    class Meta:
        model = Ans
        fields = ('getQns','answer','person',)
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}


# the table displays the questions that the current use have answered.		
class AnsTable(tables.Table):
    class Meta:
        model = Ans
        fields = ('getQns','askedByWhom','answer',)
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
