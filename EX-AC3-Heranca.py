class PosGraduacao:
    def __init__(self, intituicao, curso):
        self.insituicao = intituicao
        self.curso = curso

    def get_curso(self):
        pass #na subclasse retornará a string 'Doutorado em' + nome do curso


class Doutorado(PosGraduacao):
    def __init__(self, instituicao, curso, tese=None):
        super(). __init__(instituicao, curso)
        self.__tese = tese

    def get_curso(self): #retornado
        return f'Doutorado em {self.curso}'

    def get_tese(self):
        return self.__tese

    def set_tese(titulo):
        self.__tese = titulo

doutorado1 = Doutorado('Faculdade Impacta', 'Análise e Desenvolvimento de Sistemas', 'Título da Tese')
print(doutorado1.get_tese())



    
