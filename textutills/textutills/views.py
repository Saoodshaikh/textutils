# i have created this file - saood
from django.http import HttpResponse
from django.shortcuts import render 

#def index(request):
    #return HttpResponse('''<h1>Saud</h1> <a
#href="https://youtu.be/AepgWsROO4k?list
#=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django CodeWithHerry</a>><br> 
#<a href ="https://help.instagram.com/758461854832783/?helpref=uf_share">instagram login</a>>''')
                        
#def about(request):
    #return HttpResponse("about saud bhai")
def index(request):
    return render(request, 'index.html')      
def analyze(request):
    #GET the text
    djtext=request.POST.get('text','default')    
    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    # check whichcheckbox is on
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed +char
        params= {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #analyze the text
        #return render(request,'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed +char.upper()
        params= {'purpose':'change to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html', params)
    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed= analyzed + char
        params= {'purpose':'Removed Newlines','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==""):
                analyzed = analyzed +char    
        params = {'purpose':'extra space removed','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params) 
    if (charcount=="on"):
        analyzed = ""
        count=0
        for i in djtext:
            count += 1
            analyzed = count    
        params={'purpose':'charcount','analyzed_text':analyzed} 
        #djtext = analyzed
        #return render(request,'analyze.html',params)
    if(removepunc !="on" and fullcaps !="on" and newlineremover !="on" and extraspaceremover !="on" ):
        return HttpResponse("please select any operation and try again")
        
    return render(request,'analyze.html',params)
        
                 
    #else:
        #return HttpResponse("Error")   

#def Capitalizedfirst(request):
    #return HttpResponse("Capitalizedfirst")
#def newlineremove(request):
    #return HttpResponse("newlineremove") 

#def spaceremove(request):
    #return HttpResponse("spaceremove <a href='/'>back</a>") 

#def charcount(request):
    #return HttpResponse("charcount")