import mongoengine as mongo


class SupplierAndWarehouseTransaction(mongo.Document):
    supplier_id = mongo.StringField(required=True)
    warehouse_id = mongo.StringField(required=True)
    product_id = mongo.StringField(required=True)
    quantity_supplied = mongo.IntField(required=True)
    supply_price = mongo.FloatField(required=True)
    sale_price = mongo.FloatField(required=True)
    supplied_date = mongo.DateTimeField(required=True)

    meta = {
        'collection': 'SupplierAndWarehouseTransaction',  # نام کالکشن در MongoDB
        'ordering': ['-supplied_date']
    }

    def __str__(self):
        return f"{self.name} - {self.price}"

