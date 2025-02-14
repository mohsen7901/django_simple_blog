from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from website.forms import ContactForm, NewsletterForm
from website.models import Newsletter

def index_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            subscribed_emails = list(Newsletter.objects.all().values_list('email', flat=True))
            if form.email not in subscribed_emails:
                form.save()
                msg = "Your email address has been successfully received!"
                messages.add_message(request, messages.SUCCESS, msg)
                return HttpResponseRedirect('/')
            else:
                msg = "You have already subscribed in our Newsletter."
                messages.add_message(request, messages.WARNING, msg)
        else:
            msg = "Something went wrong! Try again."
            messages.add_message(request, messages.ERROR, msg)

    form = NewsletterForm()
    context = {'form':form}
    return render(request, 'website/index.html', context)

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Your message has been successfully received!"
            messages.add_message(request, messages.SUCCESS, msg)
        else:
            msg = "Something went wrong! Try again."
            messages.add_message(request, messages.ERROR, msg)

    form = ContactForm()
    context = {'form':form}
    return render(request, 'website/contact.html', context)
