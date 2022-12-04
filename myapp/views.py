from .models import Person
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import GeeksForm
from .forms import WordForm
from .models import Document
from pdfminer.high_level import extract_text
from django.views.generic import CreateView
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import redirect


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
            return render(request, 'myapp/input_url.html', context)
        url = form.cleaned_data['geeks_field']
        print(url)
        context['url'] = url
        # リダイレクト先のパスを取得する
        redirect_url = reverse('top')

        # パラメータのdictをurlencodeする。複数のパラメータを含めることも可能
        parameters = urlencode({'url': url})

        # URLにパラメータを付与する
        urlwithparam = f'{redirect_url}?{parameters}'
        return redirect(urlwithparam)
    return render(request, "myapp/input_url.html", context)


def top(request):
    url = request.GET.get('url')  # urlの値を取得
    form = WordForm(request.POST)
    context = {'form': form, 'url': url}
    # todo ここでurl動画を取得できるので、繋ぐならここ
    return render(request, 'myapp/index.html', context)
