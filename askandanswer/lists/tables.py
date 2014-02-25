# askandanswer/tables.py
import django_tables2 as tables
from lists.models import Qns

class QnsTable(tables.Table):
    class Meta:
        model = Qns
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
