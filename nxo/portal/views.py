from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .upload import UploadFileForm



def index(request):
    return HttpResponse("Hello, world. You're at the portal index.")


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponse('file uploaded')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

