from django.shortcuts import render, redirect
from .models import Articles, TimeTable, Gallery
from .forms import WriteForm

def index(request):
    return render(request, 'main/index.html')

def index2(request):
    gallery = Gallery.objects.all()
    return render(request, 'main/index2.html', {'gallery': gallery})

def index3(request):
    new = Articles.objects.all()
    print(new)
    return render(request, 'main/index3.html', {'new': new})


def index4(request):
    return render(request, 'main/index4.html')

def index5(request):
    timetable = TimeTable.objects.all()
    return render(request, 'main/index5.html',{'timetable': timetable})

def write(request):

    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = WriteForm
    return render(request, 'main/write.html', {'form': form})
# Create your views here.





