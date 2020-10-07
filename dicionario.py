nome = input('Digite o nome do estudante: ')
nota01 = float(input('Digite o valor da nota 1: '))
nota02 = float(input('Digite o valor da nota 2: '))

estudante = {'nome': nome, 'nota01':nota01, 'nota02':nota02}

media = (estudante['nota01'] + estudante['nota02'])/2 

estudante['media'] = media


print(estudante)