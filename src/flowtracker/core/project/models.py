class EjercicioContable:
    def __init__(self, name, date_start, date_end, description="", plan=None, state="abierto"):
        self.name = name
        self.date_start = date_start
        self.date_end = date_end
        self.id = self.calculate_id(name)
        self.description = description
        self.plan = plan
        self.state = state

    @staticmethod
    def calculate_id(name: str):
        encoded_name = name.encode('utf-8')
        hash_object = hashlib.sha256(encoded_name)
        return hash_object.hexdigest()

    def to_dict(self):
        return {
            "name": self.name,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "id": self.id,
            "description": self.description,
            "plan": self.plan,
            "state": self.state
        }