url = https://economia.awesomeapi.com.br/json/last/USD-BRL

indice_interrrogacao = urb.find('?')
url_base = urb[:indice_interrrogacao]

url_parametros = url [indice_interrrogacao + 1:]
print(urb_parametros)

parametros_busca = 'moedadestino'
indice_parametro = url_parametros.find(parametros_busca)
indice_valor = indice_parametro+ len(parametros_busca) + 1
valor = url_parametros[indice_valor:]


print(valor)