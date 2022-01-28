class Aluno:

    def __init__(self: object, codigo: int, nome: str, nota1: float, nota2: float) -> None:
        self.__codigo: int = codigo
        self.__nome: str = nome
        self.__nota1: float = nota1
        self.__nota2: float = nota2

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def nota1(self: object) -> float:
        return self.__nota1

    @property
    def nota2(self: object) -> float:
        return self.__nota2

    @property
    def media(self: object) -> float:
        media: float = ((self.__nota1 + (2*self.__nota2))/3)
        return media

    @property
    def aprovado(self: object) -> str:
        if self.media >= 6:
            return 'SIM'
        if self.media < 6:
            return 'NÃO'

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nNota 1: {self.nota1} \nNota 2: {self.nota2} \nMédia: {self.media} \nAprovado: {self.aprovado}'



        