from django.shortcuts import render, get_object_or_404, redirect
from .forms import FeedbackForm
from .models import Order, OrderItem, Feedback
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

def thanks(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render(request, 'thanks.html',{'customer_order': customer_order})
    
# reviews
def submit_feedback(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.order = order
            feedback.save()
            return redirect('order:thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'order/feedback_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def latest_feedbacks(request):
    latest_feedbacks = Feedback.objects.order_by('-timestamp')[:5]
    return render(request, 'latest_reviews.html', {'latest_feedbacks': latest_feedbacks})

class orderHistory(LoginRequiredMixin, View):
    def get (self, request):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order_details = Order.objects.filter(emailAddress=email)
        return render(request, 'order/orders_list.html', {'order_details': order_details})

class orderDetail(LoginRequiredMixin, View):
    def get(self, request, order_id):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order = Order.objects.get(id=order_id, emailAddress=email)
            order_items = OrderItem.objects.filter(order=order)

        return render(request, 'order/order_detail.html', {'order': order, 'order_items': order_items})   
          