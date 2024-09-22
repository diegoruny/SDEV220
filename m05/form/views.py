from django.shortcuts import render
from .form import ContactForm


# Create your views here.
def contact_form(request):
    if request.method != 'POST':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            context = {'form': form}
            return render(request, 'static/form.html', context)

    context = {'form': form}
    return render(request, 'static/form.html', context)


def form(request):
    return render(request, 'static/form.html')
