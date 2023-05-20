
from django.shortcuts import render
from leads.models import Lead
from django.contrib import messages

def leadAction(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('status') and request.POST.get('phone') and request.POST.get('states') and request.POST.get('city') and request.POST.get('zip'):
            saverecord = Lead()
            saverecord.first_name = request.POST.get('first_name')
            saverecord.last_name = request.POST.get('last_name')
            saverecord.status = request.POST.get('status')
            saverecord.phone = request.POST.get('phone')
            saverecord.state = request.POST.get('state')
            saverecord.city = request.POST.get('city')
            saverecord.zip_code = request.POST.get('zip')
            saverecord.save()
            messages.success(request, 'inserted successfully....')
            return render(request, 'leadscreatelead.html') #react app name
    else:
        return render(request, 'leadscreatelead.html')