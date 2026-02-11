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
        subparsers = self.parser.add_subparsers(dest="command")

        parser_acc = subparsers.add_parser("acc", help="Comandos relacionados con cuentas contables")
        acc_subparsers = parser_acc.add_subparsers(dest="acc_action")

        acc_list = acc_subparsers.add_parser("list", help="Listar todas las cuentas contables")
        acc_list.add_argument("-n", "--name", type=str, help="Nombre de la cuenta")
        acc_list.add_argument("-v", "--verbose", action="store_true", default=False, help="Muestra información adicional")
        
        acc_add = acc_subparsers.add_parser("add", help="Crear una cuenta contable")
        acc_add.add_argument("-n", "--name", required=True, type=str, help="Nombre de la cuenta")
        acc_add.add_argument("-t", "--type", required=True, type=str, choices=["fijo", "variable"], default="variable",help="Tipo de cuenta (fijo o variable)")
        acc_add.add_argument("-s", "--special", action="store_true", default=False, help="Si se incluye, es una cuenta especial")

        acc_rm = acc_subparsers.add_parser("rm", help="Borrar una cuenta contable")
        acc_rm.add_argument("-n", "--name", required=True, type=str, help="Nombre de la cuenta")
    
    def run(self):
        self.setup_commands()
        args = self.parser.parse_args()

        if args.command == "acc":
            if args.acc_action == "list":
                self.list_accounts(args)
            elif args.acc_action == "add":
                self.controller.create_account(args.name, args.type, args.special)
            elif args.acc_action == "rm":
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