from django.shortcuts import render, redirect, get_object_or_404
from .models import CalorieEntry
from .forms import CalorieEntryForm

def index(request):
    entries = CalorieEntry.objects.all().order_by('-date')
    total_calories = sum(entry.calories for entry in entries)
    return render(request, 'tracker/index.html', {'entries': entries, 'total_calories': total_calories})

def add_entry(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CalorieEntryForm()
    return render(request, 'tracker/add_entry.html', {'form': form})

def delete_entry(request, entry_id):
    entry = get_object_or_404(CalorieEntry, pk=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('index')
    return render(request, 'tracker/delete_entry.html', {'entry': entry})
