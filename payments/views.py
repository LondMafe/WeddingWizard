# In payments/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CreditCard
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.

def payments(request):
    # Your payment processing logic here
    return render(request, 'payments/payment.html')

@login_required
@require_http_methods(["POST"])
def creditCardPayment(request):
    if request.method == 'POST':
        card_holder = request.POST.get('cardHolder')
        card_number = request.POST.get('cardNumber')
        expiration_date = request.POST.get('expirationDate')
        cvv = request.POST.get('cvv')

        # You should add error handling and data validation here
        new_card = CreditCard(
            cardHolder=card_holder,
            cardNumber=card_number,
            expirationDate=expiration_date,
            cvv=cvv,
            user=request.user  # Linking the card to the logged-in user
        )
        new_card.save()
        
        # Redirect to the payment done page
        return redirect('payments:paymentDone')

    # If the request is not POST, you can redirect the user or show an error
    return HttpResponse("Invalid request", status=400)


def paymentDone(request):
    return render(request, 'payments/paymentDone.html')
