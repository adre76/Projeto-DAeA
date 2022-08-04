# PROJETO APLICADO: Data Architecture &amp; Analysis

### Predição de personalidade baseada no indicador MBTI.

------------

**Objetivo:** Através de um texto digitado pelo usuário, determinar sua personalidade, baseado em um aprendizado de máquina cuja fonte são postagens do Twitter (em inglês).

**Descrição:**
O Myers Briggs Type Indicator (MBTI sigla em inglês) é um sistema de tipo de personalidade que divide os seres humanos em 16 tipos de personalidades distintas, em 4 eixos:

- Introversão (I) – Extroversão (E)
- Intuição (N) - Detecção (S)
- Pensando (T) – Sentindo (F)
- Julgando (J) – Percebendo (P)

Como exemplo, podemos dizer que alguém que tenha o perfil de introversão, intuição, pensador e percepção seria rotulado como "INTP" no sistema MBTI.

É um dos testes de personalidade mais populares do mundo. É usado para fins de negócios, online, para diversão, para pesquisa e muito mais.

------------

### Dataset
Como base de treinamento, usei um dataset de 8676 registros contendo apenas dois campos (type e posts) por linha, com textos extraídos do Twitter (em inglês) já classificados pelo MBTI.

**Fonte:** https://www.kaggle.com/datasets/datasnaek/mbti-type?resource=download

**Descritivo da base:** 

| type        | posts                        |
|-------------|------------------------------|
| Código MBTI | Texto de postagem no Twitter |

------------

### Método de aprendizado
Especificamente, para cada termo em nosso conjunto de dados, calcularemos uma medida chamada Term Frequency, Inverse Document Frequency (tf-idf). Usaremos sklearn.feature_extraction.text.TfidfVectorizer para calcular um vetor tf-idf para cada uma das narrativas, com a seguinte parametrização:

- sublinear_df: True. Está configurado para usar uma forma logarítmica para a frequência.
- min_df: É o número mínimo de documentos em que uma palavra deve estar presente para ser mantida.
- norm: 12. Garante que todos os nossos vetores de características tenham uma norma euclidiana de 1.
- ngram_range: 1,2. Indica que queremos considerar unigramas e bigramas.
- stop_words: english. Remove todos os pronomes comuns da lingua ( "a", "the", ...) para reduzir o número de recursos ruidosos.