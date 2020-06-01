# Análise exploratória dos dados do Covid-19 no estado do Ceará

Este repositório trata-se de uma análise realizada nos dados do Coronavírus 19 referente ao estado do Ceará. 

## Onde conseguir os dados?

![ce-SUS](https://user-images.githubusercontent.com/17646546/83458857-a49c0180-a439-11ea-9f60-8ca994680a22.png)

Existe uma API pública do IntegraSUS sobre dados relacionados ao boletim epidemiológico covid-19 do estado do Ceará.

#### Download .CSV

O arquivo [download_dataset.py](https://github.com/rubnsbarbosa/covid19-analysis/blob/master/download_dataset.py) gera um arquivo .CSV 

> GET https://indicadores.integrasus.saude.ce.gov.br/api/casos-coronavirus

## Visualização em Janeiro

No primeiro gráfico notamos o número de casos por municípios 

![Captura de Tela 2020-06-01 às 18 32 41](https://user-images.githubusercontent.com/17646546/83459938-a8308800-a43b-11ea-9b52-25598158ab6d.png)

No segundo gráfico notamos o número do início dos sintomas em cada dia de janeiro. 

![Captura de Tela 2020-06-01 às 18 32 11](https://user-images.githubusercontent.com/17646546/83460001-c7c7b080-a43b-11ea-9082-0f2aca5d5e9a.png)

## Tabela da quantidade de pessoas contaminadas em Janeiro

Se 21 pessoas que foram confirmadas com coronavírus apresentaram os sintomas em 01/01/2020 e sabemos que os sintomas aparecem em torno de 14 ou 15 dias depois da contaminação, logo as pessoas pegaram a doença ainda em Dezembro de 2019. 

| Data do Início dos Sintomas        | Quantidade de Pacientes Contaminados           | 
| ------------- |:-------------:| 
| 2020-01-01 |  21 | 
| 2020-01-02 |    3 | 
| 2020-01-05 |    2 |
| 2020-01-06 |    4 |
| 2020-01-08 |    3 |
| 2020-01-09 |    3 |
| 2020-01-10 |    2 |
| 2020-01-12 |    1 |
| 2020-01-13 |    2 |
| 2020-01-14 |    1 |
| 2020-01-15 |    5 |
| 2020-01-17 |    1 |
| 2020-01-18 |    6 |
| 2020-01-19 |    2 |
| 2020-01-20 |    9 |
| 2020-01-21 |    2 |
| 2020-01-22 |    3 |
| 2020-01-23 |    3 |
| 2020-01-25 |    3 |
| 2020-01-26 |    1 |
| 2020-01-30 |    5 |
| 2020-01-31 |    1 |

## + Análises de dados do Covid-19

Para acompanhar outras análises veja o arquivo [covid19-analysis.ipynb](https://github.com/rubnsbarbosa/covid19-analysis/blob/master/covid19-analysis.ipynb). 
