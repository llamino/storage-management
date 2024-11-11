from .models import Order, OrderItem, ProductData


class CommandHandler:
    def create_order(self, user_id, product_items):
        """
        ایجاد یک سفارش جدید و محاسبه کل قیمت بر اساس قیمت محصولات و تعداد
        """
        order = Order.objects.create(user_id=user_id, total_price=0, order_state='pending')
        total_price = 0

        for item in product_items:
            product = ProductData.objects.get(product_id=item['product_id'])
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity']
            )
            total_price += product.price * item['quantity']

        # به‌روزرسانی قیمت کل سفارش پس از ایجاد آیتم‌ها
        order.total_price = total_price
        order.save()
        return order

    def update_order_status(self, order_id, new_status):
        """
        به‌روزرسانی وضعیت سفارش
        """
        order = Order.objects.get(id=order_id)
        order.order_state = new_status
        order.save()
        return order