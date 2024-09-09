from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'Luxury Glow',
        'name': 'Yemima Clara Nainggolan',
        'kelas': 'pbp b'
    }

    return render(request, "main.html", context)
