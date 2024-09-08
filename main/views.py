from django.shortcuts import render

def show_main(request):
    context = {
        'app name' : 'Luxury Glow',
        'name': 'Yemima Clara Nainggolan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
