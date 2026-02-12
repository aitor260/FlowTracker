from flowtracker.core.account import CuentaContable

class PlanContable:
    def __init__(self, *account_list: CuentaContable):
        self.__accounts: dict[str, CuentaContable] = {}
        for account in account_list:
            self.add_account(account)
    
    # Getters
    def get_accounts(self):
        return self.__accounts

    # Setters
    def set_accounts(self, accounts: dict[str, CuentaContable]):
        self.__accounts = accounts

    # Functions
    def add_account(self, account: CuentaContable):
        self.__accounts[account.get_id()] = account

    def remove_account(self, account: CuentaContable):
        self.__accounts.pop(account.get_id())

    # Output
    def __str__(self):
        return "\n".join(str(account) for account in self.__accounts.values())