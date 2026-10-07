from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100, widget=forms.EmailInput)
    message = forms.CharField(widget=forms.Textarea)

    def sendMessage(request):
        return 'mensagem enviada'
    


