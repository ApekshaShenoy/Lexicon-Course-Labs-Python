from django.shortcuts import render
from .forms import SupportTicketForm

def ticket_view(request):
    form = SupportTicketForm()

    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            print("Full name:", form.cleaned_data['full_name'])
            print("Email:", form.cleaned_data['email'])
            print("Message:", form.cleaned_data['message'])
            print("Category:", form.cleaned_data.get('category'))

    return render(request, 'SupportApp/ticket.html', {'form': form})

