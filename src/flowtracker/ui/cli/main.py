from flowtracker.ui.cli.view_cli import *
from flowtracker.ui.controller import Controller
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

        parser_proj = subparsers.add_parser("ejer", help="Comandos relacionados con las gestión de ejercicios")
        proj_subparsers = parser_proj.add_subparsers(dest="proj_action")

        proj_create = proj_subparsers.add_parser("create", help="Crear un ejercicio")
        proj_create.add_argument("-n", "--name", type=str, help="Nombre del ejercicio")
        proj_create.add_argument("-s", "--start", type=str, help="Fecha de inicio del ejercicio")
        proj_create.add_argument("-e", "--end", type=str, help="Fecha de fin del ejercicio")
        proj_create.add_argument("-d", "--description", type=str, help="Descripción del ejercicio")
        proj_create.add_argument("-v","--verbose", action="store_true", default=False, help="Muestra información adicional")
    
    def run(self):
        self.setup_commands()
        args = self.parser.parse_args()

        if args.command == "acc":
            if args.acc_action == "list":
                list_accounts(args, self.controller.get_accounts())
            elif args.acc_action == "add":
                create_account(self.controller.create_account(args.name, args.type, args.special))
            elif args.acc_action == "rm":
                self.controller.delete_account(args)
        elif args.command == "ejer":
            if args.proj_action == "create":
                view_create_project(self.controller.create_project(args))
        else:
            self.parser.print_help()

def main(args=None):
    app = CLI()
    app.run()