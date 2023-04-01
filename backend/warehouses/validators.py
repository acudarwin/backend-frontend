from django.core.exceptions import ValidationError

def validator_type(value):
    if value != "input" or value != "output":
        raise ValidationError("Type must be input or output")

def validator_quantity(value):
    if value <= 0:
        raise ValidationError("Quantity must be greater than 0")