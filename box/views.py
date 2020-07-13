from django.shortcuts import render, HttpResponse,redirect
from .forms import document_file 

from .models import DropBox

# Create your views here.
def index(request):

    context = {
        'data':DropBox.objects.all(),
       
    }

    return render(request,'index.html',context)



def add_file(request):

    if request.method == 'POST':
        forms = document_file(request.POST, request.FILES)
        
        if forms.is_valid():
            uname = forms.cleaned_data['name'] 
            ufile = forms.cleaned_data['dfiles']
                       
            dbmain = DropBox(name=uname, dbfile=ufile)
            
            dbmain.save()

            

        
        
        return redirect('/')


        

    else:
        
        forms = document_file()

        context = {
            'form': forms
        }
        

    return render(request,'file.html',context)



def add_notes(request):

    return HttpResponse('notes')