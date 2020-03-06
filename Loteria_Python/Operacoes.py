import random;
print('----------Loteria Python----------');

primeiroValorSorteio = random.randint(1, 60);
segundoValorSorteio = random.randint(1, 60);
terceiroValorSorteio = random.randint(1, 60);
quartoValorSorteio = random.randint(1, 60);
quintoValorSorteio = random.randint(1, 60);
sextoValorSorteio = random.randint(1, 60);

campoPrimeiroValorAposta = input('Digite o primeiro valor da aposta');
campoSegundoValorAposta = input('Digite o segundo valor da aposta');
campoTerceiroValorAposta = input('Digite o terceiro valor da aposta');
campoQuartoValorAposta = input('Digite o quarto valor da aposta');
campoQuintoValorAposta = input('Digite o quinto valor da aposta');
campoSextoValorAposta = input('Digite o sexto valor da aposta');

if(
primeiroValorSorteio == int(campoPrimeiroValorAposta) and
segundoValorSorteio == int(campoSegundoValorAposta) and
terceiroValorSorteio == int(campoTerceiroValorAposta) and
quartoValorSorteio == int(campoQuartoValorAposta) and
quintoValorSorteio == int(campoQuintoValorAposta) and
sextoValorSorteio == int(campoSextoValorAposta)
):
    print('Ganhou');
else:
    print('Perdeu');

print('Numeros da loteria');
print(
'[' + str(primeiroValorSorteio) + ']',
'[' + str(segundoValorSorteio) + ']',
'[' + str(terceiroValorSorteio) + ']',
'[' + str(quartoValorSorteio) + ']',
'[' + str(quintoValorSorteio) + ']',
'[' + str(sextoValorSorteio) + ']'
);

print('Numeros da aposta');
print(
'[' + str(campoPrimeiroValorAposta) + ']',
'[' + str(campoSegundoValorAposta) + ']',
'[' + str(campoTerceiroValorAposta) + ']',
'[' + str(campoQuartoValorAposta) + ']',
'[' + str(campoQuintoValorAposta) + ']',
'[' + str(campoSextoValorAposta) + ']'
);
