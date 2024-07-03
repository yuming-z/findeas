from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_weakMACD(value):
    if value != 0 and value != 1 and value != -1:
        raise ValidationError(
            _('%(value)s is not a valid weakMACD'),
            params={'value': value},
        )
    
def validate_one_hot_encoding(value):
    if value != 0 and value != 1:
        raise ValidationError(
            _('%(value)s is not a valid one-hot-encoding'),
            params={'value': value},
        )