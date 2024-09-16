from django.shortcuts import render, redirect
from main.forms import SkincareMakeupEntryForm
from main.models import SkincareMakeupEntry

def show_main(request):
    skincare_makeup_entries = SkincareMakeupEntry.objects.all()
    context = {
        'app' : 'Luxury Glow',
        'name': 'Yemima Clara Nainggolan',
        'kelas': 'PBP B'
    }

    return render(request, "main.html", context)

def skincare_makeup_entry(request):
    form = SkincareMakeupEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)
