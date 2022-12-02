from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import GeeksForm
from .models import Document
from .forms import DocumentForm
from pdfminer.high_level import extract_text


def index(request):
    documents = Document.objects.all()
    return render(request, 'myapp/index.html', {'documents': documents})


def upload(request):
    if request.method == 'POST' and request.FILES.get('testfile'):
        myfile = request.FILES.get('testfile')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        txt = extract_text('media/'+filename)
        print(txt)
        return render(request, 'myapp/upload.html', {'uploaded_file_url': uploaded_file_url, 'txt': txt})
    return render(request, 'myapp/upload.html')


def input_url(request):
    form = GeeksForm(request.POST)
    context = {'form': form}
    if request.POST:
        if not form.is_valid():
            # データ不正でフォーム再描画
            context = {'form': form}
            return render(request, 'myapp/form.html', context)
        url = form.cleaned_data['geeks_field']
        print(url)
        context['url'] = url
    return render(request, "myapp/input_url.html", context)
