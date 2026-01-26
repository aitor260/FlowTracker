from controller.Controller import Controller
import argparse

class CLI:
    def __init__(self):
        self.controller = Controller()
        self.parser = argparse.ArgumentParser(
            prog="FlowTracker",
            description="Una app en Python para automatizar la contabilidad personal. ",
            epilog="Desarrollada por Juan Orts y Aitor Pascual."
        )
    
    def setup_commands(self):
        subparsers = self.parser.add_subparsers(dest="command", help="Comando a ejecutar")

        list_accounts = subparsers.add_parser("list-accounts", help="Listas todas las cuentas contables")
        list_accounts.add_argument("-n", "--name", type=str, help="Nombre de la cuenta")
        list_accounts.add_argument("-v", "--verbose", action="store_true", default=False, help="Muestra información adicional")

        create_account = subparsers.add_parser("create-account", help="Crea una cuenta contable")
        create_account.add_argument("-n", "--name", type=str, help="Nombre de la Cuenta Contable")
        create_account.add_argument("-t", "--type", type=str, choices=["fijo", "variable"], default="variable",help="Tipo de cuenta (fijo o variable)")
        create_account.add_argument("-s", "--special", action="store_true", default=False, help="Si se incluye, es una cuenta especial")

        delete_account = subparsers.add_parser("delete-account", help="Borra una cuenta contable")
        delete_account.add_argument("-n", "--name", type=str, help="Nombre de la Cuenta Contable")
    
    def run(self):
        self.setup_commands()
        args = self.parser.parse_args()

        if args.command == "list-accounts":
            self.list_accounts(args)
        elif args.command == "create-account":
            self.controller.create_account(args.name, args.type, args.special)
        elif args.command == "delete-account":
            self.controller.delete_account(args.name)
        else:
            self.parser.print_help()

    def list_accounts(self, args):
        w_name = 30 
        w_type = w_special = 10
        w_id = 64

        header = f"{'NOMBRE':<{w_name}} {'TIPO':<{w_type}} {'ESPECIAL':<{w_special}}"
        if args.verbose:
            header += f" {'ID':<{w_id}}"
        
        print(header)
        print("=" * len(header))

        accounts = self.controller.get_accounts()
        for account in accounts:
            if account.get_special():
                special = "No"
            else:
                special = "Sí"
            line = f"{account.name:<{w_name}} {account.type.capitalize():<{w_type}} {special:<{w_special}}"
            if args.verbose:
                line += f" {account.id:<{w_id}}"
            print(line)

        print("\n")
        print("[Total de cuentas: ", str(len(accounts)) + "]")