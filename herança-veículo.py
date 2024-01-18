class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Veiculo_registrado(Veiculo):
    def __init__(self, marca, modelo, placa):
        super().__init__(marca, modelo)
        self.placa = placa

class Moto(Veiculo_registrado):
    def __init__(self, placa, guidao):
        super(). __init__(placa)
        self.guidao = guidao
        

class Carro(Veiculo_registrado):
    def __init__(self, placa, portas):
        super().__init__(placa)
        self.portas = portas

class CarroCombustão(Carro):
    def __init__(self, portas, tanque):
        super().__init__(portas)
        self.tanque = tanque

class CarroEletrico(Carro):
    def __init__(self, portas, bateria):
        super().__init__(portas)
        self.bateria = bateria

#------------------------------------------------


class Veiculo_nao_registrado(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

class Bicicleta(Veiculo_nao_registrado):
    def __init__(self, material, marchas):
        super().__init__()
        self.material = material
        self.marchas = marchas
        

