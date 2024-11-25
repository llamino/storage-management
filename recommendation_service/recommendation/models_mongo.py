import mongoengine as mongo

class OrderRecommendationHistory(mongo.Document):
    recommendation_product_id = mongo.StringField(required=True)
    user_id = mongo.StringField(required=True)
    recommendation_date = mongo.DateTimeField(required=True)
    was_purchased = mongo.BooleanField(default=False)

    meta = {
        'collection': 'order_recommendation_history',
        'ordering': '-supplied_date'
    }
    def __str__(self):
        return {self.recommendation_product_id}

class InteractionTypePerUser(mongo.Document):
    interaction_type = mongo.StringField(required=True) #related to title in IntractionType collection
    user_id = mongo.StringField(required=True)
    product_id = mongo.StringField(required=True)
    interaction_date = mongo.DateTimeField(required=True)
    meta = {
        'collection': 'InteractionTypePerUser', 'ordering': ['-intraction_date']
    }

class InteractionType(mongo.Document):
    title = mongo.StringField(required=True, primary_key=True)
    description = mongo.StringField(required=True)
    meta ={
        'collection': 'IntractionType', 'ordering': ['title']
    }