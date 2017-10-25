import django_tables2 as tables
from .models import Vm

class VmTable(tables.Table):
    class Meta:
        model = Vm
        # add class="paleblue" to <table> tag
        attrs = {'class': 'table'}