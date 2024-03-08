#!/usr/bin/env python
# coding: utf-8

# In[86]:
def distancia_levenshtein(s1, s2):
    # Criar uma matriz para armazenar os resultados dos subproblemas
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar a primeira coluna e a primeira linha da matriz
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Preencher a matriz dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            custo_substituicao = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # Deleção
                           dp[i][j - 1] + 1,         # Inserção
                           dp[i - 1][j - 1] + custo_substituicao) # Substituição
                                                                                    

    return dp[m][n]








def encontrar_sujeito(frase):
    # Supondo uma lista muito básica de verbos comuns (em suas formas infinitivas)
    verbos_comuns = [ "estar", "fazer", "poder", "dizer", "saber",
    "querer", "dever", "falar", "deixar", "pensar", "sentir", "chegar", "conhecer", "viver",
    "achar", "passar", "ficar", "voltar", "pedir", "ouvir", "trabalhar", "esperar", "precisar", "entrar",
    "sair", "aceitar", "escrever", "começar", "terminar", "esquecer", "lembrar", "pagar", "ganhar",
    "perder", "enviar", "receber", "levar", "trazer", "usar", "criar", "contar", "mostrar", "tentar",
    "precisar", "parecer", "ficar", "deixar", "acabar", "começar", "falar", "andar", "correr", "abrir",
    "fechar", "melhorar", "piorar", "amor", "odiar", "duvidar", "pensar", "cuidar", "morrer", "matar",
    "salvar", "ajudar", "gostar", "adorar", "preferir", "necessitar", "custar", "valer", "medir", "pesar",
    "discutir", "aceitar", "recusar", "aumentar", "diminuir", "nascer", "crescer", "parar", "continuar", "mudar",
    "vencer", "perdoar", "escolher", "decidir", "descrever", "subir", "descer", "ganhar", "perder", "procurar",
    "encontrar", "explicar", "entender", "pensar", "saber", "concluir", "formar", "olhar", "escutar", "morar"
]

    palavras = frase.lower().split()
    dist = 0
    distb = -1
    sujeito =""
    # Tentativa rudimentar de identificar o sujeito como a primeira palavra antes do verbo principal
    for i, palavra in enumerate(palavras):
        for verbo in verbos_comuns:
            a=distancia_levenshtein(palavra, verbo)
            if a < 3:
                # Retornar a palavra imediatamente antes do verbo encontrado, se houver
                dist = distancia_levenshtein(palavra, verbo)
                if distb == -1:
                    distb = dist
                print(distancia_levenshtein(palavra, verbo))
                if distb >= dist:
                    distb = dist
                    verboo = palavra
                    print(verbo)
                    sujeito = frase.lower().split(verboo)
                    print(sujeito)
                    sujeito = sujeito[0]
    print(verboo)
    if sujeito != "":
        print("O sujeito é:" + sujeito )
    else:
        print("Não foi possivel encontra o sujeito")
        
# Testando a função com uma frase simples
frase = "O cachorro correu pelo parque."
sujeito = encontrar_sujeito(frase)


# In[87]:


frase = "Eu gosto de laranja"
sujeito = encontrar_sujeito(frase)


# In[88]:


frase = "Eu cresci em Uberlandia"
sujeito = encontrar_sujeito(frase)


# In[89]:


frase = "O Paulo gosta de vc"
sujeito = encontrar_sujeito(frase)


# In[90]:


frase = "Ele melhorou muito isso"
sujeito = encontrar_sujeito(frase)


# In[91]:


frase = "Aquele homem velho mora naquela casa"
sujeito = encontrar_sujeito(frase)


# In[11]:




