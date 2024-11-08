import pandas as pd

class Aluno:
    def __init__(self, Nome, Nascimento, Sexo, Serie, CEP, CPF, Mae, Pai, Responsavel, TelResp, Necessidades):
        self.Nome = Nome
        self.Nascimento = Nascimento
        self.Sexo = Sexo
        self.Serie = Serie
        self.CEP = CEP
        self.CPF = CPF
        self.Mae = Mae
        self.Pai = Pai
        self.Responsavel = Responsavel
        self.TelResp = TelResp
        self.Necessidades = Necessidades

    def ver(self):
        print(f"Informações do Aluno: \n Nome: {self.Nome} \n Data de Nascimento: {self.Nascimento} \n")
        print(f"Sexo: {self.Sexo} \n Série: {self.Serie} \n CEP: {self.CEP} CPF: {self.CPF} \n")
        print(f"Mãe: {self.Mae} \n Pai: {self.Pai} \n Responsável: {self.Responsavel} \n")
        print(f"Telefone do Responsável: {self.TelResp} \n Necessidades: {self.Necessidades}\n")


def salvar_alunos_csv(lista_alunos, nomi="alunos.csv"):
    dados = [{
        "Nome": aluno.Nome,
        "Nascimento": aluno.Nascimento,        
        "Sexo": aluno.Sexo,
        "Serie": aluno.Serie,
        "CEP": aluno.CEP,
        "CPF": aluno.CPF,
        "Mae": aluno.Mae,
        "Pai": aluno.Pai,
        "Responsavel": aluno.Responsavel,
        "TelResp": aluno.TelResp,
        "Necessidades": aluno.Necessidades
    } for aluno in lista_alunos]
    
    df = pd.DataFrame(dados)
    df.to_csv(nomi, index=False)
    print(f"Dados salvos no arquivo {nomi}.")

Aluno1 = Aluno(
    Nome='João da Silva', Nascimento='15/03/2010', Sexo='Masculino',
    Serie='9º Ano "A" ', CEP='12345-678', CPF='111.222.333-00',
    Mae='Maria Oliveira', Pai='José da Silva', Responsavel='Ana Souza',
    TelResp='(11) 98765-4321', Necessidades='Nenhuma'
)

Aluno2 = Aluno(
    Nome='Marina Angelo', Nascimento='15/03/2015', Sexo='Feminino',
    Serie='4º ano ‘B’', CEP='12345-678', CPF='123.456.789-00',
    Mae='Ana Angelo', Pai='João Angelo', Responsavel='Ana Angelo',
    TelResp='(11) 94515-4321', Necessidades='Acompanhamento devido ao Espectro Autista'
)

Aluno3 = Aluno(
    Nome='Pedro Santos', Nascimento='10/08/2009', Sexo='Masculino',
    Serie='1º Serie ‘A’', CEP='54321-987', CPF='987.654.321-00',
    Mae='Carla Santos', Pai='Marcos Santos', Responsavel='Yuri Santos ("Avô")',
    TelResp='(21) 99999-8888', Necessidades='Alergia a amendoim'
)


lista_padrao = [Aluno1,Aluno2,Aluno3]

def carregar_alunos_csv(nomi="alunos.csv"):
    try:
        df = pd.read_csv(nomi)
        lista_alunos = [Aluno(**dados) for dados in df.to_dict(orient="records")] 
        print(f"{len(lista_alunos)} alunos carregados do arquivo {nomi}.") 
        return lista_alunos
    except FileNotFoundError:
        print(f"O arquivo {nomi} não foi encontrado. Iniciando com lista de alunos padrão")
        return lista_padrao

def validar_cpf(cpf):
    if len(cpf) != 14:
        return False
    elif cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False
   
    else:
        return True

def validar_cep(cep):
    if len(cep) != 9:
        return False
    elif cep[5] != '-':
        return False

    else:
        return True
    
def validar_tel(TelResp):
    if len(TelResp) != 14:
        return False
    elif TelResp[0] != '(' or TelResp[3] != ')' or TelResp[4] != '9':
        return False
    
    else :
        return True
    
def validar_Nascimento(nasc):
    if len(nasc) != 10:
        return False
    if nasc[2] != '/' or nasc[5] != '/':
        return False
    else:
        return True

def novocad(aluno):
    lista_alunos.append(aluno)
    salvar_alunos_csv(lista_alunos)
    print('\n \n \n \n Para voltar ao menu digite qualquer coisa')
    vai = input()
    print('\n \n \n \n \n')
    menu()

def editcad(cpf, novos_dados):
    for aluno in lista_alunos:
        if aluno.CPF == cpf:
            aluno.__dict__.update(novos_dados)
            break
    salvar_alunos_csv(lista_alunos)
    print('\n \n \n \n Para voltar ao menu digite qualquer coisa')
    vai = input()
    print('\n \n \n \n \n')
    menu()

def remocad(cpf):
    for aluno in lista_alunos:
        if aluno.CPF == cpf:
            lista_alunos.remove(aluno)
            break
    salvar_alunos_csv(lista_alunos)
    print('\n \n \n \n Para voltar ao menu digite qualquer coisa')
    vai = input()
    print('\n \n \n \n \n')
    menu()
    
def menu():
     print('='*70,"\n \n \n", ' '*28, "Escola Municipal \n",' '*20, "Profº Bernardo Lemos Sochodolak \n \n")
     print(' '*26,'-'*24, "\n", ' '*25, "| 1 - Ver Cadastro     |")
     print( "\n", ' '*25, "| 2 - Editar Cadastros |")
     print( "\n", ' '*25, "| 3 - Novo Cadastro    |")
     print( "\n", ' '*25, "| 4 - Remover cadastro |")
     print( "\n", ' '*25, "| 5 - Saiba Mais       |")
     print( "\n", ' '*25, "| 6 - Fechar           |")
     print(' '*26,'-'*24," \n \n \n", " "*15)
     escolha = input("")
     
     if escolha == '1':
        vercad()

     elif escolha == '2':
        cpf = input('Digite o CPF do aluno que deseja editar: ')
        while validar_cpf(cpf) == False:
            print("CPF incorreto ou não cadastrado \n Tente Novamente ou Digite 0 para retornar ao menu ")
            cpf = input('Digite o CPF do aluno que deseja editar: ')
            if cpf == '0':
                print('\n \n \n \n \n')
                menu()

        novos_dados = {}
        print('Deixe em branco os campos que não deseja alterar.')
        nome = input('Novo nome: ')
        if nome:
            novos_dados['Nome'] = nome
            nascimento = input('Nova data de nascimento: ')
        if nascimento:
            novos_dados['Nascimento'] = nascimento
            sexo = input('Novo sexo: ')
        if sexo:
            novos_dados['Sexo'] = sexo
            serie = input('Nova série: ')
        if serie:
            novos_dados['Serie'] = serie
            cep = input('Novo CEP: ')
        if cep:
            novos_dados['CEP'] = cep
            mae = input('Nova mãe: ')
        if mae:
            novos_dados['Mae'] = mae
            pai = input('Novo pai: ')
        if pai:
            novos_dados['Pai'] = pai
            responsavel = input('Novo responsável: ')
        if responsavel:
            novos_dados['Responsavel'] = responsavel
            telresp = input('Novo telefone do responsável: ')
        if telresp:
            novos_dados['TelResp'] = telresp
            necessidades = input('Novas necessidades: ')
        if necessidades:
            novos_dados['Necessidades'] = necessidades
        editcad(cpf, novos_dados)
    
     elif escolha == '3':
       ncpf = input("Digite o CPF do Novo Aluno : [Formato XXX.XXX.XXX-XX] :")
       while validar_cpf(ncpf) == False:
            print("CPF incorreto \n Tente Novamente ou Digite 0 para retornar ao menu")
            ncpf = input('Digite o CPF do novo aluno : ')
            if ncpf == '0':
                print('\n \n \n \n \n')
                menu()
       nasc = input("Digite a data de Nascimento do aluno : [Formato DD/MM/AAAA] :")
       while validar_Nascimento(nasc) == False:
            print("Data de Nascimento incorreto \n Tente Novamente ou Digite 0 para retornar ao menu ")
            nasc = input('Digite a data de Nascimento do novo aluno : ')
            if nasc == '0':
                print('\n \n \n \n \n')
                menu()
       ncep = input("Digite o CEP do aluno : [Formato XXXXX-XXX] :")
       while validar_cep(ncep) == False:
            print("CEP Incorreto \n Tente Novamente ou Digite 0 para retornar ao menu ")
            ncep = input('Digite p CEP do novo aluno : ')
            if ncep == '0':
                print('\n \n \n \n \n')
                menu()
       ntel = input("Digite o telefone do Responsavel : [Formato (XX)XXXXX-XXXX] :")
       while validar_tel(ntel) == False:
            print("Nº de telefone incorreto \n Tente Novamente ou Digite 0 para retornar ao menu ")
            ntel = input('Digite o telefone do novo aluno : ')
            if ntel == '0':
                print('\n \n \n \n \n')
                menu()
         
        
       novo_aluno = Aluno(
       Nome = input('Digite o Nome do Novo Aluno : '),
       Nascimento  =  nasc,
       Sexo  =  input('Digite o sexo : '),
       Serie  =  input('Digite a serie do aluno : '),
       CEP  =  ncep,
       CPF  =  ncpf,
       Mae =  input('Digite o nome da Mãe : '),
       Pai =  input('Digite o nome do Pai : '),
       Responsavel =  input('Digite o Nome do Responsavel : '),
       TelResp =  ntel,
       Necessidades =  input('Digite as Necessidades especiais do aluno, Alergias, Acessebilidades Necessarias Etc : '),
      ) 
       novocad(novo_aluno)

     elif escolha == '4':
        print("Para escolher o Aluno a ser removido do cadastro digite o cpf do aluno : \n")
        print("Seguindo no modelo Padrão Ex = 'XXX.XXX.XXX-XX' ")
        cpf = input("")
        while validar_cpf(cpf) == False:
            print("CPF incorreto \n Tente Novamente ou Digite 0 para retornar ao menu ")
            cpf = input('Digite a data de Nascimento do novo aluno : ')
            if cpf == '0':
                print('\n \n \n \n \n')
                menu() 
        else:
            remocad(cpf)
    
     elif escolha == '5':
        saiba()

     elif escolha == '6':
        salvar_alunos_csv(lista_alunos)
        exit()

     else:
       print("X"*70, "\n Escolha Invalida - Tente Novamente \n", "X"*70, "\n \n \n \n")
       menu()
 
def vercad():
     for aluno in lista_alunos:
        print('='*70,"\n \n")
        aluno.ver()
        
     print('\n \n \n \n Para voltar ao menu digite qualquer coisa')
     vai = input()
     print('\n \n \n \n \n')
     menu() 


def remocad(cpf):
    for aluno in lista_alunos:
        if aluno.CPF == cpf:
            lista_alunos.remove(aluno)       
            break
    salvar_alunos_csv(lista_alunos)           
    print('\n \n \n \n Para voltar ao menu digite qualquer coisa')
    vai = input()
    print('\n \n \n \n \n')
    menu()

def saiba():
    print("Escola Profº Bernardo Lemos Sochodolak \n Um exemplo de Escola Ficticia Baseada nos 3 Nomes dos intregantes do Grupo, Alexsandro Lemos, Bernardo Kuster Ragugnetti  e Eduardo Sochodolak")
    print("\n A Ideia é desenolver um sistema de Cadastro e Armazenamento de alunos podendo ver os cadastrados, adicionar novos alunos, editar informações e remover cadastros.")
    print("\n Uso de funções def para separar o codigo, listas para armazenar os alunos, classes para dinamizar cada um dos alunos e usos de estrutura de repetição \n Para voltar ao menu digite qualquer coisa")
  
    vai = input()
    print('\n \n \n \n \n')
    menu()


lista_alunos = carregar_alunos_csv()
salvar_alunos_csv(lista_alunos)  

menu() 
