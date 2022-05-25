'''
Equipe titular
Venceslau está treinando uma equipe de futebol Pequi Futebol Clube (Pequi FC) e encontra dificuldades para escalar um time titular ideal. A equipe possui um elenco com n jogadores, em que o i-ésimo jogador possui nível técnico (habilidade) ai. Quanto maior é o valor de ai, mais habilidoso é o jogador em questão.

O Pequi FC está disputando a quinta divisão do Campeonato Goiano, em que cada equipe deve levar exatamente 11 jogadores a campo, definindo o time titular. Já para o banco de reservas, o clube pode levar, no máximo, 11 jogadores. Como Venceslau é um treinador com características ofensivas, ele sempre  escala os melhores jogadores (os mais habilidosos) para o time titular e leva para o banco de reservas os jogadores mais habilidosos do elenco que não foram escalados como titulares. Infelizmente, alguns atletas do elenco podem não chegar a serem relacionados para o jogo.

Considerando que a soma da habilidades dos jogadores titulares e reservas sejam t e r, respectivamente, escreva um programa que determine a maior diferença possível entre t e r. Vale lembrar que, Venceslau sempre leva a maior quantidade possível de jogadores para os jogos, sendo sempre possível levar ao menos um time titular (11 jogadores) e um jogador reserva.

Entrada
A primeira linha da entrada contém um número inteiro n (12≤n≤102), indicando a quantidade de jogadores no plantel do Pequi FC. A segunda linha contém n números inteiros separados por espaço, a1,a2,…,an (1≤ai≤100), indicando a habilidade de cada jogador do plantel.

Saída
Imprima um número inteiro que expressa a maior diferença possível entre as somas das habilidades dos jogadores dos times titular e reserva.
'''
numero_de_jogadores = int(input())
lista_de_habilidades = list(map(int, input().split()))

lista_de_habilidades.sort()

lista_de_maiores_habilidades = lista_de_habilidades[len(lista_de_habilidades):numero_de_jogadores - 12:-1]
lista_de_maiores_habilidades.sort()

lista_de_menores_habilidades = lista_de_habilidades[:len(lista_de_habilidades) - 11]
if len(lista_de_menores_habilidades) > 11:
    lista_de_menores_habilidades = lista_de_menores_habilidades[len(lista_de_habilidades):len(lista_de_menores_habilidades) - 12:-1]

soma_maiores_habilidades = sum(lista_de_maiores_habilidades)
soma_menores_habilidades = sum(lista_de_menores_habilidades)

diferencatotal = soma_maiores_habilidades - soma_menores_habilidades

print(diferencatotal)


    