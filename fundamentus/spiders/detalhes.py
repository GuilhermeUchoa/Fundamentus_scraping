import scrapy


class DetalhesSpider(scrapy.Spider):
    name = 'detalhes'
    allowed_domains = ['fundamentus.com.br/']

    with open('tickers.txt','r') as arq:
        arquivo = arq.read()

    tickers = arquivo.split()
    
    start_urls= ['https://www.fundamentus.com.br/detalhes.php?papel='+str(i) for i in tickers]



    def parse(self, response):

        valores_brutos = response.css('span.txt::text').extract()
        valores = []
        #Substituir valores, que estam com - mas nao sao negativos
        for i in range(len(valores_brutos)):
            if valores_brutos[i] == '\n-' :
                valores.append(valores_brutos[i].replace('\n-',''))
            elif valores_brutos[i] == '-':
                valores.append(valores_brutos[i].replace('-',''))
            else:
                valores.append(valores_brutos[i])
                
        setor_subsetor = response.css('span.txt a::text').extract()
        oscilacoes = response.css('font::text').extract()
       
        if len(valores_brutos) == 110:

            yield{

                "Papel" : valores[1],
                "Cotação" : valores[3].replace(",",".").replace("\n",""),
                "Tipo" : valores[5],
                "Data ult cot" : valores[7],
                "Empresa" : valores[9],
                "Min 52 sem" : valores[11].replace(",",".").replace("\n",""),
                "Setor" : setor_subsetor[0],
                "Max 52 sem" : valores[14].replace(",",".").replace("\n",""),
                "Subsetor" : setor_subsetor[1],
                "Vol $ méd (2m)" : valores[17].replace(",",".").replace("\n",""),

                "Valor de mercado" : valores[19].replace(".","").replace("\n",""),
                "Últ balanço processado" : valores[21].replace(".","").replace("\n",""),
                "Valor da firma" : valores[23].replace(".","").replace("\n",""),
                "Nro. Ações" : valores[25].replace(".","").replace("\n",""),
                
                "Dia%" : oscilacoes[0].replace(",",".").replace("%","").replace("\n",""),
                "P/L" : valores[30].replace(",",".").replace("\n",""),
                "LPA" : valores[32].replace(",",".").replace("\n",""),
                "Mês%" : oscilacoes[1].replace(",",".").replace("%","").replace("\n",""),
                "P/VP" : valores[35].replace(",",".").replace("\n",""),
                "VPA" : valores[37].replace(",",".").replace("\n",""),
                "30 dias%" : oscilacoes[2].replace(",",".").replace("%","").replace("\n",""),
                "P/EBIT" : valores[40].replace(",",".").replace("\n",""),
                "Marg. Bruta%" : valores[42].replace(",",".").replace("%","").replace("\n",""),
                "12 meses%" : oscilacoes[3].replace(",",".").replace("\n","").replace("%",""),
                "PSR" : valores[45].replace(",",".").replace("\n",""),
                "Marg. EBIT" : valores[47].replace(",",".").replace("\n","").replace("%",""),
                "Ano_Atual%" : oscilacoes[4].replace(",",".").replace("\n","").replace("%",""),
                "P/Ativos" : valores[50].replace(",",".").replace("\n",""),
                "Marg. Líquida%" : valores[52].replace(",",".").replace("\n","").replace("%",""),
                "Ano_Atual(-1)%" : oscilacoes[5].replace(",",".").replace("\n","").replace("%",""),
                "P/Cap. Giro" : valores[55].replace(",",".").replace("\n",""),
                "EBIT / Ativo%" : valores[57].replace(",",".").replace("\n","").replace("%",""),
                "Ano_Atual(-2)%" : oscilacoes[6].replace(",",".").replace("%","").replace("\n",""),
                "P/Ativ Circ Liq" : valores[60].replace(",",".").replace("\n",""),
                "ROIC%" : valores[62].replace(",",".").replace("%","").replace("\n",""),
                "Ano_Atual(-3)%" : oscilacoes[7].replace(",",".").replace("%","").replace("\n",""),
                "Div. Yield%" : valores[65].replace(",",".").replace("%","").replace("\n",""),
                "ROE%" : valores[67].replace(",",".").replace("%","").replace("\n",""),
                "Ano_Atual(-4)%" : oscilacoes[8].replace(",",".").replace("%","").replace("\n",""),
                "EV / EBITDA" : valores[70].replace(",",".").replace("\n",""),
                "Liquidez Corr" : valores[72].replace(",","."),
                "Ano_Atual(-5)%" : oscilacoes[9].replace(",",".").replace("%","").replace("\n",""),
                "EV / EBIT" : valores[75].replace("\n",""),
                "Div Br/ Patrim" : valores[77].replace(",",".").replace("\n",""),
                "Ano_Atual(-6)%" : "NaN",
                "Cres. Rec (5a)" : valores[79].replace(",",".").replace("%","").replace("\n",""),
                "Giro Ativos" : valores[81].replace(",",".").replace("\n",""),
                
                "Ativo" : valores[84].replace(".","").replace("\n",""),
                "Depósitos": "NaN" ,
                "Cart. de Crédito": "NaN" ,
                "Dív. Bruta" : valores[86].replace(".",""),
                "Disponibilidades" : valores[88].replace(".",""),
                "Dív. Líquida" : valores[90].replace(".",""),
                "Ativo Circulante" :valores[92].replace(".",""),
                "Patrim. Líq" : valores[94].replace(".",""),
                                    
                "Receita Líquida_12meses" : valores[99].replace(".",""),
                "Receita Líquida_3meses" : valores[101].replace(".",""),
                "EBIT_12meses" : valores[103].replace(".",""),
                "EBIT_3meses" : valores[105].replace(".",""),
                "Result Int Financ_12meses": "NaN" ,
                "Result Int Financ_3meses": "NaN" ,
                "Rec Serviços_12meses": "NaN" ,
                "Rec Serviços_3meses": "NaN" ,
                "Lucro Líquido_12meses" : valores[107].replace(".",""),
                "Lucro Líquido_3meses" : valores[109].replace(".",""),


                
                }

                   
             
            
        elif len(valores_brutos) == 106:

            yield{

                "Papel" : valores[1],
                "Cotação" : valores[3].replace(",",".").replace("\n",""),
                "Tipo" : valores[5],
                "Data ult cot" : valores[7],
                "Empresa" : valores[9],
                "Min 52 sem" : valores[11].replace(",",".").replace("\n",""),
                "Setor" : setor_subsetor[0],
                "Max 52 sem" : valores[14].replace(",",".").replace("\n",""),
                "Subsetor" : setor_subsetor[1],
                "Vol $ méd (2m)" : valores[17].replace(",",".").replace("\n",""),

                "Valor de mercado" : valores[19].replace(".","").replace("\n",""),
                "Últ balanço processado" : valores[21].replace(".","").replace("\n",""),
                "Valor da firma" : valores[23].replace(".","").replace("\n",""),
                "Nro. Ações" : valores[25].replace(".","").replace("\n",""),

                "Dia%" : oscilacoes[0].replace(",",".").replace("%","").replace("\n",""),
                "P/L" : valores[30].replace(",",".").replace("\n",""),
                "LPA" : valores[32].replace(",",".").replace("\n",""),
                "Mês%" : oscilacoes[1].replace(",",".").replace("%","").replace("\n",""),
                "P/VP" : valores[35].replace(",",".").replace("\n",""),
                "VPA" : valores[37].replace(",",".").replace("\n",""),
                "30 dias%" : oscilacoes[2].replace(",",".").replace("%","").replace("\n",""),
                "P/EBIT" : valores[40].replace(",",".").replace("\n",""),
                "Marg. Bruta%" : valores[42].replace(",",".").replace("%","").replace("\n",""),
                "12 meses%" : oscilacoes[3].replace(",",".").replace("\n","").replace("%",""),
                "PSR" : valores[45].replace(",",".").replace("\n",""),
                "Marg. EBIT" : valores[47].replace(",",".").replace("\n","").replace("%",""),
                "Ano_Atual%" : oscilacoes[4].replace(",",".").replace("\n","").replace("%",""),
                "P/Ativos" : valores[50].replace(",",".").replace("\n",""),
                "Marg. Líquida%" : valores[52].replace(",",".").replace("\n","").replace("%",""),
                "Ano_Atual(-1)%" : oscilacoes[5].replace(",",".").replace("\n","").replace("%",""),
                "P/Cap. Giro" : valores[55].replace(",",".").replace("\n",""),
                "EBIT / Ativo%" : valores[57].replace(",",".").replace("\n","").replace("%",""),
                "Ano_Atual(-2)%" : oscilacoes[6].replace(",",".").replace("%","").replace("\n",""),
                "P/Ativ Circ Liq" : valores[60].replace(",",".").replace("\n",""),
                "ROIC%" : valores[62].replace(",",".").replace("%","").replace("\n",""),
                "Ano_Atual(-3)%" : oscilacoes[7].replace(",",".").replace("%","").replace("\n",""),
                "Div. Yield%" : valores[65].replace(",",".").replace("%","").replace("\n",""),
                "ROE%" : valores[67].replace(",",".").replace("%","").replace("\n",""),
                "Ano_Atual(-4)%" : oscilacoes[8].replace(",",".").replace("%","").replace("\n",""),
                "EV / EBITDA" : valores[70].replace(",",".").replace("\n",""),
                "Liquidez Corr" : valores[72].replace(",","."),
                "Ano_Atual(-5)%" : oscilacoes[9].replace(",",".").replace("%","").replace("\n",""),
                "EV / EBIT" : valores[75].replace("\n",""),
                "Div Br/ Patrim" : valores[77].replace(",",".").replace("\n",""),
                "Ano_Atual(-6)%" : "NaN",
                "Cres. Rec (5a)" : valores[79].replace(",",".").replace("%","").replace("\n",""),
                "Giro Ativos" : valores[81].replace(",",".").replace("\n",""),
                
                "Ativo" : valores[84].replace(".",""),
                "Depósitos": valores[86].replace(".",""), 
                "Cart. de Crédito": valores[88].replace(".","") ,
                "Dív. Bruta" : "NaN",
                "Disponibilidades" : "NaN",
                "Dív. Líquida" : "NaN",
                "Ativo Circulante" : "NaN",
                "Patrim. Líq" : valores[90].replace(".",""),
                                    
                "Receita Líquida_12meses" : "NaN" ,
                "Receita Líquida_3meses" : "NaN" ,
                "EBIT_12meses" : "NaN" ,
                "EBIT_3meses" : "NaN" ,
                "Result Int Financ_12meses": valores[95].replace(".","") ,
                "Result Int Financ_3meses": valores[97].replace(".","") ,
                "Rec Serviços_12meses": valores[99].replace(".","") ,
                "Rec Serviços_3meses": valores[101] ,
                "Lucro Líquido_12meses" : valores[103].replace(".",""),
                "Lucro Líquido_3meses" : valores[105].replace(".",""),  

                }

