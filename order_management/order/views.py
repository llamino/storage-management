from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from .commands import CommandHandler
from .queries import QueryHandler
from .models import Order

class CreateOrderView(View):
    def post(self, request):
        command_handler = CommandHandler()
        user_id = request.POST.get('user_id')
        product_items = request.POST.getlist('product_items')  # دریافت آیتم‌های محصول

        # بررسی صحت داده‌های دریافتی
        if not user_id or not product_items:
            return HttpResponseBadRequest("Missing 'user_id' or 'product_items' in the request.")

        order = command_handler.create_order(user_id, product_items)
        return JsonResponse({'order_id': order.id, 'total_price': order.total_price})


class UpdateOrderView(View):
    def post(self, request, order_id):
        command_handler = CommandHandler()

        # دریافت وضعیت جدید سفارش از درخواست
        new_status = request.POST.get('order_state')

        # بررسی اینکه وضعیت جدید وجود داشته باشد
        if not new_status:
            return HttpResponseBadRequest("Missing 'order_state' in the request.")

        try:
            # به‌روزرسانی وضعیت سفارش با استفاده از CommandHandler
            updated_order = command_handler.update_order_status(order_id, new_status)

            # برگرداندن پاسخ به کاربر
            return JsonResponse({
                'order_id': updated_order.id,
                'new_status': updated_order.order_state,
                'total_price': updated_order.total_price
            })
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class GetOrderDetailsView(View):
    def get(self, request, order_id):
        query_handler = QueryHandler()
        try:
            order_details = query_handler.get_order_details(order_id)
            return JsonResponse(order_details)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
