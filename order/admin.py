from django.contrib import admin
from .models import Order, OrderItem, Feedback

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
    ('Food',{'fields':['food'],}),
    ('Quantity',{'fields':['quantity'],}),
    ('Price',{'fields':['price'],}),
    ]
    readonly_fields = ['food','quantity','price'] 
    can_delete = False
    max_num = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','billingName','emailAddress','created']
    list_display_links = ('id','billingName')
    search_fields = ['id','billingName','emailAddress']
    readonly_fields = ['id','token','total','emailAddress','created','billingName','billingAddress1', 
'billingCity', 'billingPostcode','billingCountry','shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']
    fieldsets = [
    ('ORDER INFORMATION',{'fields': ['id','token','total','created']}),
    ('BILLING INFORMATION', {'fields':
['billingName','billingAddress1','billingCity','billingPostcode','billingCountry','emailAddress']}),
    ('SHIPPING INFORMATION', {'fields':
['shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Order, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'timestamp')
    search_fields = ['customer_name', 'feedback_text']
    list_filter = ['timestamp']

admin.site.register(Feedback, FeedbackAdmin)