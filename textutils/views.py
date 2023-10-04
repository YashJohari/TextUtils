from django.http import HttpResponse
# import os
from django.shortcuts import render

# print(os.path.dirname)

# def index(request):
#     # file_path = os.path.join(os.path.dirname(__file__), 'one.txt')
#     with open('C:\\Users\\Lenovo\\textutils\\textutils\\one.txt', 'r') as file:
#         content = file.read()
#     return HttpResponse(content)



def index(request):
    params = {'name' : 'Harry', 'place' : 'Mars'}
    return render(request, 'index.html', params)


def analyze(request):
    flag=0
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        flag=1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

    if(fullcaps=="on"):
        flag=1
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

    if(extraspaceremover=="on"):
        flag=1
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

    if (newlineremover == "on"):
        flag=1
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

    
    if(flag==1):
        params = {'purpose': 'Changes Done!', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


# def about(request):
#     return HttpResponse("About Harry Bhai")


# def removepunc(request):
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse("remove punc <a href='/'>Back</a>")

