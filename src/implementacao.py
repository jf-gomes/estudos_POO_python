from classes import *

usuario1 = Administrador(1, 'João', 'joao@empresa.com', '12345', 'Programador', 'DTI', 'amostraJoao', 'biometriaJoao')
usuario1.emitirComando('Voz', 'abrir porta', '23/03/24')
usuario1.gerarRelatorio('Relatório de usuários')
usuario1.acessarDB('Listar')