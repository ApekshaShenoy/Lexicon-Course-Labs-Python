"""class Something:
def __init__(self,data:dict):
    self.__dict__ = data

def __str__(self):
    str_rep = ""
    for key, value in self.__dict__.items():
        str_rep += f"{key}={value}, "
    return str_rep.rstrip(", ")

def __str__(self):
    return ", ".join(f"{key}={value}" for key, value in self.__dict__.items())

{"name": "Apeksha", "age": 32}
"""
class Something:
    def __init__(self, data: dict):
        self.__dict__ = data

    def __str__(self):
        return ", ".join(f"{key}={value}" for key, value in self.__dict__.items())

{"name": "Apeksha", "age": 32}