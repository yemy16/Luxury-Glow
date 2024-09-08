from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'Luxury Glow',
        'name': 'Yemima Clara Nainggolan',
        'npm': '2306245825'
    }

    return render(request, "main.html", context)
