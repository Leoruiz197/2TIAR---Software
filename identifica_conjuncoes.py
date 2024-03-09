conjuncoes = ['ou', 'depois disso', 'por outro lado', 'por vezes', 'em geral', 'em última instância', 'logo', 'que sim', 'contudo', 'por essa razão', 'ainda assim',
 'em detrimento', 'já que', 'porquanto', 'além disso', 'sobretudo', 'do mesmo modo', 'quer dizer', 'não apenas', 'embora', 'da mesma forma', 'em conformidade',
 'nem tão pouco', 'como', 'pelo mesmo motivo', 'consequentemente', 'da mesma maneira', 'em suma', 'quanto mais', 'por esse motivo', 'de modo que', 'porém',
 'em seguida', 'em vez de', 'por isso', 'tão somente', 'em comparação', 'daí que', 'pelo contrário', 'por consequência', 'mas', 'neste ínterim', 'em última análise',
 'entretanto', 'de outra maneira', 'portanto', 'assim que', 'de forma que', 'em segundo lugar', 'quando', 'não só', 'de acordo com', 'com tudo isso', 'nem sequer',
 'assim', 'tão logo', 'apesar de', 'apesar de tudo', 'ao passo que', 'conforme', 'antes que', 'noutro sentido', 'por exemplo', 'bem como', 'enquanto isso', 'porque',
 'mesmo assim', 'com o intuito de', 'neste caso', 'apesar', 'em vez', 'a exemplo de', 'nesse ínterim', 'não obstante', 'tão pouco', 'igualmente', 'que', 'quer',
 'que nem', 'não é que', 'ao mesmo tempo', 'como resultado', 'tão quanto', 'a fim de que', 'nem por isso', 'do mesmo jeito', 'uma vez que', 'desde que', 'em vez disso',
 'por este motivo', 'com efeito', 'sendo assim', 'em síntese', 'ou seja', 'com tudo', 'em conjunto', 'em contraste', 'também', 'em virtude disso', 'ora', 'apesar disso',
 'por conseguinte', 'depois que', 'em um certo sentido', 'dado que', 'mesmo que', 'de outro modo', 'de maneira que', 'em grande parte', 'no entanto', 'por um lado',
 'caso', 'em alternativa', 'em terceiro lugar', 'em conclusão', 'tal como', 'nem', 'mas também', 'em virtude de', 'ainda que', 'em parte', 'nem sempre', 'em relação',
 'em consequência', 'tão', 'dentro do mesmo contexto', 'para que', 'seja', 'e', 'enquanto', 'em adição', 'conquanto', 'neste sentido', 'ademais', 'se', 'inclusive',
 'eventualmente', 'à vista disso', 'até que', 'em contrapartida', 'por causa de', 'todavia', 'pois', 'outra coisa', 'logo que', 'como se', 'às vezes', 'dessa forma',
 'quem sabe', 'conjuntamente', 'senão', 'ao contrário', 'quanto a isso', 'a fim de', 'de outra forma', 'quiçá', 'pelo menos', 'do contrário', 'posto que', 'ao invés',
 'como também', 'em conformidade com', 'tanto quanto', 'em particular', 'assim mesmo', 'tanto', 'nem tanto', 'visto que', 'nesse sentido', 'em igual medida',"e"]

def identificar_conjuncoes():
    def solicitar_frase():
        return input("Digite uma frase: ")

    frase = solicitar_frase()
    tokens = frase.lower().split()
    conjuncoes_encontradas = [token for token in tokens if token in conjuncoes]
    return conjuncoes_encontradas

conjuncoes_encontradas = identificar_conjuncoes()
conjuncoes_encontradas