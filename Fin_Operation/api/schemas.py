from rest_framework.schemas import AutoSchema
import coreapi
import coreschema

class FilterSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
                coreapi.Field(
                    name='accounts',
                    location='form',
                    required=False,
                    schema=coreschema.Array(description='Список id счетов')
                ),
                coreapi.Field(
                    name='amount_from',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='Минимальная сумма операции')
                ),
                coreapi.Field(
                    name='amount_to',
                    location='form',
                    required=False,
                    schema=coreschema.Integer(description='Максимальная сумма операции')
                )
        ]