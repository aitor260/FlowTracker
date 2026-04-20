from .models import CuentaContable
import flowtracker.data

def save_new_account(cuenta: CuentaContable):
    cuenta.to_dict()