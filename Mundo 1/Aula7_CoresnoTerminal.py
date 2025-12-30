# ==================================================
# AULA 7 — CORES NO TERMINAL COM CÓDIGOS ANSI
# Mundo 1 — Fundamentos do Python
# ==================================================

# No terminal do Python, podemos utilizar códigos ANSI
# para alterar a cor do texto, a cor do fundo e aplicar efeitos.

# A estrutura básica de um código ANSI é:
# '\033[' + códigos + 'm'

# IMPORTANTE:
# Sempre finalize com '\033[m' para resetar o estilo,
# evitando que o resto do terminal fique colorido.

# ==================================================
# CÓDIGOS DE CORES — TEXTO
# ==================================================

# Preto        -> \033[30m
# Vermelho     -> \033[31m
# Verde        -> \033[32m
# Amarelo      -> \033[33m
# Azul         -> \033[34m
# Roxo         -> \033[35m
# Ciano        -> \033[36m
# Branco       -> \033[37m
# Cinza claro  -> \033[90m

# ==================================================
# CÓDIGOS DE CORES — FUNDO
# ==================================================

# Fundo Preto     -> \033[40m
# Fundo Vermelho  -> \033[41m
# Fundo Verde     -> \033[42m
# Fundo Amarelo   -> \033[43m
# Fundo Azul      -> \033[44m
# Fundo Roxo      -> \033[45m
# Fundo Ciano     -> \033[46m
# Fundo Branco    -> \033[47m

# ==================================================
# CÓDIGOS DE EFEITOS
# ==================================================

# Reset / Nenhum efeito -> \033[0m
# Negrito              -> \033[1m
# Sublinhado           -> \033[4m
# Invertido            -> \033[7m

# ==================================================
# EXEMPLOS BÁSICOS DE USO
# ==================================================

print('\033[1;31;43mOlá, Mundo!\033[m')
# Texto em negrito, vermelho, com fundo amarelo

print('\033[4;34mTexto azul sublinhado.\033[m')

print('\033[7;32mTexto verde com efeito invertido.\033[m')

# ==================================================
# EXEMPLOS SIMPLES DE CORES
# ==================================================

print('\033[31mEste texto é vermelho.\033[m')
print('\033[42mEste texto tem fundo verde.\033[m')
print('\033[1;34mTexto azul em negrito.\033[m')
print('\033[4;33mTexto amarelo sublinhado.\033[m')
print('\033[7;35mTexto roxo com efeito invertido.\033[m')

# ==================================================
# COLORINDO VARIÁVEIS
# ==================================================

nome = input('Qual é o seu nome? ')

print(f'Olá, \033[1;32m{nome}\033[m! Seja bem-vindo(a)!')

# ==================================================
# EXEMPLOS PRÁTICOS DE MENSAGENS
# ==================================================

print('\033[1;34mPython é uma linguagem de programação incrível!\033[m')
print('\033[43mEste texto possui fundo amarelo.\033[m')
print('\033[4;31mCuidado! Texto vermelho e sublinhado.\033[m')
print('\033[7;36mTexto ciano com efeito invertido.\033[m')

# ==================================================
# COMBINAÇÕES AVANÇADAS
# ==================================================

print('\033[1;30;47mTexto preto em negrito com fundo branco.\033[m')
print('\033[4;33;44mTexto amarelo sublinhado com fundo azul.\033[m')
print('\033[7;35;40mTexto roxo invertido com fundo preto.\033[m')

# ==================================================
# SIMULAÇÃO DE MENSAGENS DE SISTEMA
# ==================================================

print('\033[1;31mAtenção: Este é um aviso importante!\033[m')
print('\033[42mSucesso: Operação concluída com êxito!\033[m')
print('\033[4;34mInformação: Dados carregados corretamente.\033[m')
print('\033[7;33mAlerta: Verifique os detalhes fornecidos.\033[m')
print('\033[1;36mDica: Use cores para destacar informações importantes.\033[m')
print('\033[45mMensagem destacada com fundo roxo.\033[m')
print('\033[4;32mTexto verde sublinhado para ênfase.\033[m')
print('\033[7;31mTexto vermelho invertido para chamar atenção.\033[m')

# ==================================================
# FIM DA AULA
# ==================================================
