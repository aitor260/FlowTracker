from .utils import write_json, read_json
from flowtracker.core.project.models import EjercicioContable
import uuid

class PersistenceManager:
    def __init__(self, project: EjercicioContable = None, project_path=None, last_sync=None):
        self.current_project = project
        self.project_path = project_path
        self.last_sync =last_sync
        self.session_id = self.generate_session_id()
        self.is_session_active = True

    def generate_session_id(self):
        return uuid.uuid4().hex

    def exists(self, account_id: str) -> bool:
        data = read_json(self.file_path)
        return any(item['id'] == account_id for item in data)

    def add_account(self, account: dict):
        #Aqui faltaria primero mirar a ver si está duplicado
        data = read_json(self.file_path)
        data.append(account)
        write_json(self.file_path, data)

    def get_accounts(self):
        raw_data = read_json(self.file_path)
        return [CuentaContable(**account) for account in raw_data]

    def delete_account(self, account_id: str):
        data = read_json(self.file_path)
        data = [account for account in data if account['id'] != account_id]
        write_json(self.file_path, data)

    def create_project(self, args):
      return 0  