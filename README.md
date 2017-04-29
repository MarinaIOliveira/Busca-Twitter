# Busca-Twitter
Coleta de dados via API do Twitter

Por meio da API disponibilizada pelo twitter, é possível coletar tweets realizados recentemente. No script em questão foram coletados tweets em umo raio de 50 metros em relação a latitude e longitude de um determinado ponto turístico. É realizado a requisição e armazenado em um banco noSQL (MongoDB). Caso seja gerado algum erro durante a coleta, o memso é inserido em um arquivo TXT.
