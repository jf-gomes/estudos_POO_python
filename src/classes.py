class Funcionario:
    def __init__(self, id, nome, email, senha, cargo, setor, amostraVoz, biometriaFacial):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.setor = setor
        self.amostraVoz = amostraVoz
        self.biometriaFacial = biometriaFacial

    def emitirComando(self, tipoComando, finalidade, executadoEm):
        validarComando = ValidacaoComando(tipoComando, finalidade, self.amostraVoz, self.biometriaFacial, executadoEm)
        validacao = validarComando.validar()
        if validacao != "ErroValidacao":
            print(validacao.executar())
        else:
            print('Validação falhou.')

class Administrador(Funcionario):
    def gerarRelatorio(self, tipoRelatorio):
        autenticacao = Autenticacao(self.id, self.senha)
        if autenticacao.autenticar():
            relatorio = Relatorio(tipoRelatorio)
            print(relatorio.emitir())
        else:
            print('Não foi possível emitir o relatório')

    def acessarDB(self, finalidade):
        autenticacao = Autenticacao(self.id, self.senha)
        if autenticacao.autenticar():
            acessoDB = AcessoDB('24/03/2024', self.id, finalidade)
            tiposAcessoDB = {
                'Listar': acessoDB.listarDados(),
                'Excluir': acessoDB.excluirDados(),
                'Editar': acessoDB.editarDados(),
                'Inserir': acessoDB.inserirDados()
            }
            tiposAcessoDB[finalidade]
        else:
            print('Acesso negado')

class Autenticacao:
    def __init__(self, idUsuario, senha):
        self.idUsuario = idUsuario
        self.senha = senha
    
    def autenticar(self):
        if self.idUsuario == 1 and self.senha == '12345':
            return True
        else:
            return False

class ValidacaoComando:
    def __init__(self, tipoComando, finalidade, amostraVoz, biometriaFacial, executadoEm):
        self.tipoComando = tipoComando
        self.finalidade = finalidade
        self.amostraVoz = amostraVoz
        self.biometriaFacial = biometriaFacial
        self.executadoEm = executadoEm

    def validar(self):
        if self.tipoComando == 'Voz' and self.amostraVoz == 'amostraJoao':
            comando = Comando(self.finalidade, self.executadoEm)
            return comando
        elif self.tipoComando == 'Camera' and self.biometriaFacial == 'biometriaJoao':
            comando = Comando(self.finalidade, self.executadoEm)
            return comando
        else:
            return 'ErroValidacao'
        
class Comando:
    def __init__(self, finalidade, executadoEm):
        self.finalidade = finalidade
        self.executadoEm = executadoEm

    def executar(self):
        return f"Comando para {self.finalidade} executado em {self.executadoEm}."
    
class Relatorio:
    def __init__(self, tipoRelatorio):
        self.tipoRelatorio = tipoRelatorio
    
    def emitir(self):
        return f"Relatório do tipo {self.tipoRelatorio} emitido."
    
class AcessoDB:
    def __init__(self, dataAcesso, usuario, finalidade):
        self.dataAcesso = dataAcesso
        self.usuario = usuario
        self.finalidade = finalidade

    def listarDados(self):
        if self.finalidade == 'Listar':
            print('Listando dados')
    
    def excluirDados(self):
        if self.finalidade == 'Excluir':
            print('Excluindo dados')
    
    def editarDados(self):
        if self.finalidade == 'Editar':
            print('Editando dados')
    
    def inserirDados(self):
        if self.finalidade == 'Inserir':
            print('Inserindo dados')