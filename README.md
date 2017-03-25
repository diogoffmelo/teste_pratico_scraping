# Chamada para Desenvolvedores - Time de Scraping


Solucao para o desafio de desenvolvedores scraping - intelivix

O spider na solucao procura por dados de kits de desenvolvimento para sistemas embarcados no site
digikey.com e guarda informacoes relevantes em um banco de dados. O framework __Scrapy__ e o pymongo sao assumidos instalados e corretamente configurados. Uma instancia do mongodb e assumida rodando no local host porta padrao, mas pode ser configurado em setup.py.


Para rodar o crawler 

- Utilização de `xpath` nas buscas por links (__OK__)
- Persistência das informações (__OK__)
- Submissão de formulários (__OK__)
- Tratamento de paginação (__OK__)
- Manipulação de (__OK__)
- Autenticação (__OK__)
- Utilizar logs para sinalizar ocorrências durante o __scraping__ (__OK__)


Para executar, use o comando **scrapy crawl digikey** no diretorio root do crawler.
O tempo de desenvolvimento total foi de 2 dias (duas manhas e duas tardes).


# Descricao original

Teste prático para os desenvolvedores candidatos as vagas do time de "scraping".

O teste segue descrito abaixo:

Eleger um site alvo e construir um crawler utilizando o framework __Scrapy__.

O código deverá ser disponibilizado no Github assim como as instruções
para replicar a execução do mesmo.

Demonstrar boa utilização do framework entre outras habilidades
explorando os pontos abaixo:

- Utilização de `xpath` nas buscas por links (**obrigatório**)
- Persistência das informações (Preferencialmente __PostgreSQL__, __MongoDB__ ou __RethinkDB__) (**obrigatório**)
- Submissão de formulários
- Tratamento de paginação
- Manipulação de __querystrings__
- Autenticação
- Utilizar logs para sinalizar ocorrências durante o __scraping__

Quaisquer dúvidas podem ser enviadas para arthur@intelivix.com.
O candidato deve registrar o tempo despendido para o desenvolvimento.
Não existe um escopo de tempo oficial, mas o ideal é que não ultrapasse 1 semana.
