from django.core.exceptions import ValidationError


def phone_for_user(phone):
    print(phone)
    # 87771231212 = 11, or +77771231212 = 12
    if len(phone) == 12 or len(phone) == 11:
        return
    raise ValidationError('Неправильный номер телефона! Телефон должен быть в таком формате: '
                              '+77771231212; 87771231212; Без пробелов!')
