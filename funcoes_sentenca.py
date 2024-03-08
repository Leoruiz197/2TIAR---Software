def identificar_predicado(sujeito, sentenca):
    posicao_da_palavra = sentenca.find(sujeito)
    if posicao_da_palavra == -1:
      return None
    posicao_proxima_pontuacao = sentenca.find('.', posicao_da_palavra)
    if posicao_proxima_pontuacao == -1:
      return sentenca[posicao_da_palavra + len(sujeito):]
    return sentenca[posicao_da_palavra + len(sujeito):posicao_proxima_pontuacao]
 
 
# Exemplo de uso
# sujeito = "Joao"
# sentenca = "Joao esta procurando o pé de feijao"
# predicado = identificar_predicado(sujeito, sentenca)
# print("O predicado é:", predicado)# comecem por aqui
