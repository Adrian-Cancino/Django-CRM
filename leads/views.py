from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

#View for all the leads
def lead_list(request):

    leads = Lead.objects.all()

    context = {
        "leads": leads 
    }
    return render(request, "leads/lead_list.html", context)

#View for a specefic lead
def lead_detail(request, pk):

    lead = Lead.objects.get(id=pk)

    context = {
        "lead": lead
    }

    return render(request, "leads/lead_detail.html", context)

# View for create a new lead
def lead_create(request):

    form = LeadModelForm()

    if request.method == "POST":

        form = LeadModelForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

