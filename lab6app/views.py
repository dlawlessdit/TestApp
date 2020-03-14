from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

def testlang(request):
        return HttpResponse(_('Welcome to language translation!'))


def index(request):
# This method uses the page request to determine which page to return
    # create context
    context = {}
    pagereq=str(request.path)

    if "index2" in pagereq:
        return render(request,'index2.html',context)
    elif "index3" in pagereq:
        return render(request,'index3.html',context)
    elif "index4" in pagereq:
        return render(request,'index4.html',context)
    elif "index5" in pagereq:
        return render(request,'index5.html',context)
    else:
        return render(request,'index.html',context)


def portfolio(request):

    # create context
    context = {}
    # create context
    context = {}
    pagereq=str(request.path)

    if "portfolio-2" in pagereq:
        return render(request,'portfolio-2.html',context)
    elif "portfolio-3" in pagereq:
        return render(request,'portfolio-3.html',context)
    elif "portfolio-4" in pagereq:
        return render(request,'portfolio-4.html',context)
    elif "portfolio-detail" in pagereq:
        return render(request,'portfolio-detail.html',context)
    else:
        return render(request,'404.html',context)