from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import QuoteRequestForm
from .models import QuoteRequest


# Create your views here.
def index(request):
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            service = form.cleaned_data['service']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            submition = QuoteRequest.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                service=service,
                phone=phone,
                message=message,

            )
            submition.save()
             # return redirect('success_page')  # Başarılı sayfasına yönlendirin
    else:
        form = QuoteRequestForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    return render(request, 'project.html')


def blogs(request):
    return render(request, 'blog.html')
