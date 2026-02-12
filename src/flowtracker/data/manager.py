from flowtracker.core import CuentaContable
from .utils import write_json, read_json

class PersistenceManager:
    def __init__(self):
        self.file_path = "./data_files/accounts.json"

    def exists(self, account_id: str) -> bool:
        data = read_json(self.file_path)
        return any(item['id'] == account_id for item in data)

    def save_account(self, account: CuentaContable):
        data = read_json(self.file_path)
        data.append(account.to_dict())
        write_json(self.file_path, data)

    def get_accounts(self):
        raw_data = read_json(self.file_path)
        return [CuentaContable(**account) for account in raw_data]

    def delete_account(self, account_id: str):
        data = read_json(self.file_path)
        data = [account for account in data if account['id'] != account_id]
        write_json(self.file_path, data)