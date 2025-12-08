Os dados, se eles forem mensagens, eles terão delimitadores especiais. 

O delimitador especial no Python é a aspa simples (') ou a aspa dupla ("). A grande parte da comunidade utiliza a aspa simples para delimitar mensagens.
                                                   
Todos os comandos são funções e todas as funções possuem parênteses.    

Exemplo:
print('Olá, Mundo!') aparecerá a mensagem Olá, Mundo! na tela.

No Python, números não precisam de aspas. Eles são reconhecidos como números automaticamente.

Exemplo:
print(7+4) ou 7+4 resultará na soma dos números, ou seja, 11.

Porém para expressar números como mensagens, é necessário o uso de aspas.

Exemplo:
print('7+4') resultará na mensagem '7+4' e não na soma dos números.

E se isolar as aspas em cada número?

Exemplo:
print('7'+'4') ou '7'+'4' resultará na junção das mensagens, ou seja, '74'.

Para combinar tudo isso e guardar as informações em um lugar, utilizamos as variáveis.

No caso do Python, toda variável é um objeto. Um objeto é uma estrutura que guarda informações e possui características e comportamentos.

Toda variável pode receber valores, o "recebe" é representado pelo sinal de igual (=).

Exemplo:
nome='Guanabara' guarda a mensagem 'Guanabara' na variável nome.
idade=18 guarda o número 18 na variável idade.  
peso=80.5 guarda o número 80.5 na variável peso.

Para exibir o conteúdo de uma variável, basta utilizar o comando print() com o nome da variável dentro dos parênteses.

Exemplo:
print(nome, idade, peso) resultará na mensagem Guanabara 18 80.5

Para que essas variáveis não sejam fixas, podemos utilizar a função input() para receber dados do usuário.

Exemplo:
nome=input('Qual é o seu nome? ') exibirá a mensagem "Qual é o seu nome?" na tela e aguardará o usuário digitar uma resposta. A resposta digitada será armazenada na variável nome.

idade=input('Quantos anos você tem? ') exibirá a mensagem "Quantos anos você tem?" na tela e aguardará o usuário digitar uma resposta. A resposta digitada será armazenada na variável idade.

peso=input('Qual é o seu peso? ') exibirá a mensagem "Qual é o seu peso?" na tela e aguardará o usuário digitar uma resposta. A resposta digitada será armazenada na variável peso.

E para comentários, utilizamos o símbolo jogo da velha (#). Tudo que estiver após esse símbolo em uma linha será ignorado pelo interpretador Python.