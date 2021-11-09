from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required
from . import forms

def events_list(request):
    events = Event.objects.all().order_by('date');
    return render(request, 'events/events_list.html', { 'events': events })

def event_detail(request, slug):
    # return HttpResponse(slug)
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_detail.html', { 'event': event })

@login_required(login_url="/accounts/login/")
def event_create(request):
    if request.method == 'POST':
        form = forms.CreateEvent(request.POST, request.FILES)
        if form.is_valid():
            # save event to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('events:list')
    else:
        form = forms.CreateEvent()
    return render(request, 'events/event_create.html', { 'form': form })
