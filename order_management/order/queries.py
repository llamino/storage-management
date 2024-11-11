from .models import Order, OrderItem


class QueryHandler:
    def get_order_details(self, order_id):
        """
        دریافت جزئیات کامل سفارش، شامل آیتم‌ها و اطلاعات مربوط به محصول
        """
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)

        return {
            'order_id': order.id,
            'user_id': order.user_id,
            'total_price': order.total_price,
            'order_state': order.order_state,
            'items': [
                {
                    'product_id': item.product.product_id,
                    'name': item.product.name,
                    'price': item.product.price,
                    'quantity': item.quantity
                }
                for item in order_items
            ]
        }

    def list_orders_by_user(self, user_id):
        """
        دریافت لیستی از سفارشات یک کاربر خاص
        """
        orders = Order.objects.filter(user_id=user_id)
        return [
            {
                'order_id': order.id,
                'total_price': order.total_price,
                'order_state': order.order_state,
                'pub_at': order.pub_at
            }
            for order in orders
        ]