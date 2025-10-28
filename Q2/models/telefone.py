class Telefone:
    def __init__(self, identificador, numero):
        self.identificador = identificador
        self.numero = numero

    def __str__(self):
        return f"{self.identificador}: {self.numero}"
