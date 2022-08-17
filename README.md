# PROJETO APLICADO: Data Architecture &amp; Analysis
### Professor: Nicolas Marcos de Moraes Oliveira - Curso: MBA em BI & Data Science
### Aluno: André Luís dos Reis Pereira - Matrícula: 2022.05.17910-9


------------

**Descrição:**
Códigos Python que fazem a ingestão de dados históricos de espaço em disco dos servidores de backup e gera gráficos para .

**Fonte:** Dados coletados dos servidores de backup da Superintendência de Operações do SERPRO.

### Datasets
Arquivos .csv separados por informações de backup e informações de volumetria de disco dos servidores de backup.

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