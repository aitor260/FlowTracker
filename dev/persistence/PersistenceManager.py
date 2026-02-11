from domain.CuentaContable import CuentaContable
import persistence.FileServ as fs

class PersistenceManager:
    def __init__(self):
        self.file_path = "../.data/accounts.json"

    def exists(self, account_id: str) -> bool:
        data = fs.read_json(self.file_path)
        return any(item['id'] == account_id for item in data)

    def save_account(self, account: CuentaContable):
        data = fs.read_json(self.file_path)
        data.append(account.to_dict())
        fs.write_json(self.file_path, data)

    def get_accounts(self):
        raw_data = fs.read_json(self.file_path)
        return [CuentaContable(**account) for account in raw_data]

    def delete_account(self, account_id: str):
        data = fs.read_json(self.file_path)
        data = [account for account in data if account['id'] != account_id]
        fs.write_json(self.file_path, data)