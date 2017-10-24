from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .upload import FileUpload
from .transform import extract_vms

def index(request):

    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the portal index.")


def upload(request):
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()
            extract_vms(new_file)
            return HttpResponse('WIP: Redirect to assessment workflow page.')
    else:
        form = FileUpload()
    return render(request, 'upload.html', {
        'form': form
    })

