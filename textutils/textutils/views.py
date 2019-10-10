# created self
from django.http import HttpResponse
from django.shortcuts import render
# routing work
def index(request):
  
   info = {"name":"Sonu", "place":"Delhi"}
   return render(request,"index.html", info)

def removepunc(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')



    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed



    if (fullcap == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed



    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
             analyzed = analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed


    if(spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):

             # It is for if a extraspace is in the last of the string
             if char == djtext[-1]:
                 if not (djtext[index] == " "):
                     analyzed = analyzed + char

             elif not (djtext[index] == " " and djtext[index + 1] == " "):
                 analyzed = analyzed + char

             params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
             djtext = analyzed


    if (removepunc != "on" and fullcap != "on" and newlineremover != "on" and spaceremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, "Analiyze.html", params)

def abt(request):
    return HttpResponse('''<h1>JavaTpoint ji</h1> <a href="https://www.javatpoint.com/django-apache-configuration">javaTpoint</a>
    <br><h1>W3 Python</h1> <a href="https://www.w3schools.com/default.asp">W3school</a>''')

def contact(request):
    return HttpResponse("mobile mo.9641900005")

def city(request):
   return HttpResponse("Panipat")