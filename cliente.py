class cliente(object):
    def __init__(self, nome, cpf, rg, telefone, celular, email, endereco, numero, bairro, complemento):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.celular = celular
        self.email = email
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_rg(self):
        return self.rg

    def get_telefone(self):
        return self.telefone

    def get_celular(self):
        return self.celular

    def get_email(self):
        return self.email

    def get_endereco(self):
        return self.endereco

    def get_numero(self):
        return self.numero

    def get_bairro(self):
        return self.bairro

    def get_complemento(self):
        return self.complemento
