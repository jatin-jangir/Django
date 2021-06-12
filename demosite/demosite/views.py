from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   
    return render(request,'index.html')

def about(request):
    return HttpResponse('<h1> we use heading tag here </h1> <br> <a href="http://127.0.0.1:8000/"><button type="button">back to home</button></a>')

def search(request):
    return HttpResponse("searching "+'<a href="http://127.0.0.1:8000/"><button type="button">back to home</button></a>')
    
def analyse(request):
    str=request.POST.get('text','default')
    rp=request.POST.get('removepunc','off')
    cf=request.POST.get('capital','off')
    rn=request.POST.get('removenum','off')
    rs=request.POST.get('removespace','off')
    pur=''
    punc='''!@#$%^&*()_+-=<>,.?/~`;:'"\|'''
    if(rp=='on'):
        pur='remove punctuations'
        for c in str:
            if c in punc:
                str=str.replace(c,'')
    if(rs=='on'):
        pur=pur+' remove spaces'
        for c in str:
            if c == ' ':
                str=str.replace(c,'')
    if(rn=='on'):
        pur=pur+' remove numbers'
        str=''.join([i for i in str if not i.isdigit()])
    if(cf=='on'):
        pur=pur+' capitalize first'
        str=str.capitalize()

    params={'purpose':pur,'analysed_text':str}
    return render(request,'textUtil.html',params)
