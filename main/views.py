from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245825',
        'name': 'Yemima Clara Nainggolan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
