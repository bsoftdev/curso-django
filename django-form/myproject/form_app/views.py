from django.shortcuts import render, redirect
from form_app.form import ContactForm

# Create your views here.

def homeView(request):
    return render(request, 'register/home.html')


def contactView(request):

        if request.method == 'POST':
            form = ContactForm(request.POST)  
            if form.is_valid():
                form.sendMessage()
                return redirect('success')
        else:
             form = ContactForm()
        return render(request, 'register/registation.html', {'form':form})
            
def successview(request):
    return render(request, 'register/success.html')

    
