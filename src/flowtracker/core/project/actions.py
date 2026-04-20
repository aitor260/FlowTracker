from flowtracker.data import PersistenceManager

def project_creation(args):
    pm = PersistenceManager()
    pm.create_project(args["name"], args["date_start"], args["date_end"], args["description"])
    return 0