# pages/views.py

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
import io
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Client
from pages.forms import ClientForm
from .models import Client
from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa

def client_form_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('success')  # تأكد من أن 'success' هو اسم URL الصحيح
    else:
        form = ClientForm()
    return render(request, 'pages/client_form.html', {'form': form})

def success_view(request):
    # Define what you want to do on successful form submission
    return render(request, 'pages/success.html')

def print_receipt(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    html = render_to_string('pages/receipt.html', {'client': client})
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# pages/views.py
def print_receipt(request, client_id):
    client = Client.objects.get(pk=client_id)
    context = {
        'client': client,
    }
    html = render_to_string('pages/receipt.html', context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{client_id}.pdf"'
    
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.StringIO(html), result)
    if not pdf.err:
        response.write(result.getvalue())
        return response
    return HttpResponse('Error generating PDF', status=500)
