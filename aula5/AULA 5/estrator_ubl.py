class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()


        def sanitiza_url(self,url):
            return url.strip()
        
        def valida_url(self):
            if self.url =="":
                raise ValueError("a URL esta vazia")



estrator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")