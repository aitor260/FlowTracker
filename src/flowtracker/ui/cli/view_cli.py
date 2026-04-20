def list_accounts(args, accounts):
    w_name = 30 
    w_type = w_special = 10
    w_id = 64

    header = f"{'NOMBRE':<{w_name}} {'TIPO':<{w_type}} {'ESPECIAL':<{w_special}}"
    if args.verbose:
        header += f" {'ID':<{w_id}}"
    
    print(header)
    print("=" * len(header))

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

def create_account(ret):
    if ret == 0:
        print("¡Cuenta creada con éxito!")
    elif ret == -1:
        print("¡Error! No se ha podido crear la cuenta.")
    elif ret == -2:
        print("Ya existe una cuenta con ese nombre. Prueba con otro.")

def view_create_project(ret):
    print("Ejercicio creado")
