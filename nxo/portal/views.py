from django.shortcuts import render, redirect

from django_tables2 import RequestConfig

# Create your views here.
#from django.http import HttpResponse
from .upload import FileUpload
from .transform import extract_vms
from .models import File, Vm
from .tables import VmTable

def index(request):

    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the portal index.")

def download(request):

    return render(request, 'download.html')


def upload(request):
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()
            extract_vms(new_file)
            return redirect('/analyze/{}'.format(request.POST['name']))
    else:
        form = FileUpload()
    return render(request, 'upload.html', {
        'form': form
    })

def analyze(request, filename=None):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    file = File.objects.filter(name=filename)[0]
    vms = Vm.objects.filter(file=file)
    if file == None:
        print("No file found")
    else:
        pp.pprint(vms)

    table = VmTable(vms)
    RequestConfig(request).configure(table)
    return render(request, 'analyze.html', {
        'table': table,
        'file': file,
        'vms': vms,
        'ram_total_gb': file.computed_ram/1024/1024/1024,
        'capacity_total_gb': file.computed_capacity/1024/1024/1024,
    })
