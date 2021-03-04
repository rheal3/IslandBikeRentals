from models.User import User
from main import ma
from marshmallow.validate import Length


class UserSchema (ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ["password"]

    username = ma.String(required=True, validate=Length(min=3))
    password = ma.String(required=True, validate=Length(min=6))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
