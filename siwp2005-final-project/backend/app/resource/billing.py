from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from model.billing import Billing
from helper.schema import BillingSchema
import helper.validator as validator

class BillingAPI(Resource):
    @jwt_required()
    def get(self, billing_id):
        billing = Billing.objects.get(id=billing_id)
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200

    @jwt_required()
    def put(self, billing_id):
        data = request.get_json()
        billing = Billing.objects.get(id=billing_id)
        billing.update(**data)
        return BillingSchema().dump(billing.reload()), 200

    @jwt_required()
    def delete(self, billing_id):        
        billing = Billing.objects.get(id=billing_id)
        billing.delete()
        return {}, 204

class BillingListAPI(Resource):
    @jwt_required()
    def get(self):
        billings = Billing.objects()
        serialized_payload = BillingSchema(many=True).dump(billings)
        return serialized_payload, 200

    @jwt_required()
    def post(self):
        serialized_payload = validator.billing_validator()
        billing = Billing(**serialized_payload)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
