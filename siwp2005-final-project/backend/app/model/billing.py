from utils import db
from model.user import User

class Billing(db.Document):
    user = db.ReferenceField(User)
    amount = db.DecimalField(required=True)
    description = db.StringField(required=True)
