# askandanswer/tables.py
import django_tables2 as tables
from lists.models import Qns,Ans

class QnsTable(tables.Table):
    class Meta:
        model = Qns
        fields = ('id','qns','getAnswer',)
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

class AnsTable(tables.Table):
    class Meta:
        model = Ans
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
