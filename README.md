# PROJETO APLICADO: Data Architecture &amp; Analysis
### Professor: Nicolas Marcos de Moraes Oliveira - Curso: MBA em BI & Data Science
### Aluno: André Luís dos Reis Pereira - Matrícula: 2022.05.17910-9


------------

**Descrição:**
Códigos Python que fazem a ingestão de dados históricos de utilização de espaço em disco dos servidores de backup e gerar gráficos para apresentação em um dashboard que dá suporte à operação e tomada de decisão sobre a escalabilidade da solução.

### Arquivos Python
- carga.py: Realiza a modelagem dos dados e os adiciona ao banco de dados para consumo em uma aplicação web.
- etl.py: Realiza a modelagem dos dados e gera gráficos que são consumidos por uma aplicação web.

### Datasets
Arquivos .csv separados por informações de backup e informações de volumetria de disco dos servidores de backup.

**Fonte:** Dados descaracterizados, coletados de uma fonta pública do governo.

**Descritivo das bases:** 

**coletas.csv**

| nodename             | datainicio               | status                       | result                      | datafim                   | server             |
|----------------------|--------------------------|------------------------------|-----------------------------|---------------------------|--------------------|
| Nodename do servidor | Data de início do backup | Status do processo de backup | Alertas gerados na execução | Data de término do backup | Servidor de backup |

**particoes.csv**

| particao         | total               | usado                    | livre                    | porcentagem                   | server             | data                     |
|------------------|---------------------|--------------------------|--------------------------|-------------------------------|--------------------|--------------------------|
| Nome da partição | Tamanho da partição | Volume usado da partição | Volume livre da partição | Porcentagem usada da partição | Servidor de backup | Data de coleta dos dados |
------------