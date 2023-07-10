# I have created this file - Abrar
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # dict1 = {'name':'Abrar', 'place':'Mars'}
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    # Get the data from FORM
    dj_text = request.POST.get('f_text', 'dafault')
    # Check the box checked
    punc_check = request.POST.get('remove_punctuation', 'off')
    cap_box = request.POST.get('uppercase', 'off')
    space_remover = request.POST.get('space_remover', 'off')
    count_chars = request.POST.get('count_words', 'off')

    analyzed_text = ""

    if punc_check == 'on':
        punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        for char in dj_text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char

        params = {'purpose': 'Remove Punctuation',
                  'analyzed_text': analyzed_text}
        dj_text = analyzed_text
        # return render(request, 'analyze-page.html', params)

    if cap_box == 'on':
        for char in dj_text:
            analyzed_text = analyzed_text + char.upper()

        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed_text}
        dj_text = analyzed_text
        # return render(request, 'analyze-page.html', params)

    if space_remover == 'on':
        for index, char in enumerate(dj_text):
            if not (dj_text[index] == " " and dj_text[index+1] == " "):
                analyzed_text = analyzed_text + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed_text}
        dj_text = analyzed_text

    if count_chars == 'on':
        words = 1
        for char in dj_text:
            if char == " " or char == "\t" or char == "\n":
                words += 1
        params = {'purpose': 'Space Remover',
                  'analyzed_text': analyzed_text, 'total_words': words}

    return render(request, 'analyze-page.html', params)

    # else:
    #     return HttpResponse("<h2>ERROE</h2>")

    # return HttpResponse("<h2>Capitalization</h2> <br> Click <a href='http://127.0.0.1:8000/'>here</a> to back home.")
