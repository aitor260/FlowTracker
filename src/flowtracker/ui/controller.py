from flowtracker.core.account.models import CuentaContable
from flowtracker.core.project.actions import project_creation
from flowtracker.data.manager import PersistenceManager

# Este módulo no debería depender de PM directamente

class Controller:
    def __init__(self):
        self.persistence_manager = PersistenceManager()

    def create_account(self, name: str, type: str, special: bool):
        nueva_cuenta = CuentaContable(name, type, special)
        
        if self.persistence_manager.exists(nueva_cuenta.id):
            return -2
        else:
            self.persistence_manager.save_account(nueva_cuenta)
            return 0

    def get_accounts(self):
        return self.persistence_manager.get_accounts()

    def delete_account(self, name: str):
        self.persistence_manager.delete_account(CuentaContable.calculate_id(name))

    def create_project(self, args):
        if project_creation(args) == 0:
            return 0