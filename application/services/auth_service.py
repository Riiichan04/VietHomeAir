from application.models import Account


def user_login(email, password):
    target_account = Account.objects.filter(email=email, password=password, status=True).first()
    return {key: getattr(target_account, key) for key in [field.name for field in Account._meta.fields if
                                                          field.name not in [
                                                              'password']]} if target_account is not None else None


def user_register(usernmame, email, password, **kwargs):
    if validate_new_user(usernmame, password):
        new_user = Account.objects.create(name=usernmame, email=email, password=password, **kwargs)
        return new_user
    return None


def validate_new_user(username, email):
    return Account.objects.filter(username=username, email=email).first() is None
