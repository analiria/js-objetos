url ="bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

url = ""
#sanitizaçao da UBL 
url = url.replace(" ", "")

if url == "":
    raise ValueError("a URL esta vazia")

# separa base e parametros
indice_interrrogacao = url.find('?')
url_base = url[:indice_interrrogacao]
url_parametros = url [indice_interrrogacao + 1:]
print(url_parametros)

#busca o valor de um o parametro
parametros_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametros_busca)
indice_valor = indice_parametro+ len(parametros_busca) + 1
indice_e_ccomercial = url_parametros.find('&', indice_valor)
if indice_e_ccomercial == -1:
 valor = url_parametros[indice_valor:]
else:
 valor = url_parametros[indice_valor: indice_e_ccomercial]


print(valor)