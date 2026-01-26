from persistence.PersistenceManager import PersistenceManager
from domain.CuentaContable import CuentaContable

class Controller:
    def __init__(self):
        self.persistence_manager = PersistenceManager()

    def create_account(self, name: str, type: str, special: bool):
        nueva_cuenta = CuentaContable(name, type, special)
        
        if self.persistence_manager.exists(nueva_cuenta.id):
            print("¡Error! Ese nombre ya está pillado. Elige otro.")

        else:
            self.persistence_manager.save_account(nueva_cuenta)
            print("Cuenta creada con éxito.")

    def get_accounts(self):
        return self.persistence_manager.get_accounts()

    def delete_account(self, name: str):
        self.persistence_manager.delete_account(CuentaContable.calculate_id(name))