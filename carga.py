#IMPORTANDO BIBLIOTECAS
from sqlalchemy import create_engine
from urllib import parse
import psycopg2, io, os, sys, warnings, shutil, errno
import pandas as pd

#

# PARAMETRIZAÇÃO DA CONEXÃO COM O BANCO DE DADOS
engine = create_engine(
  'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'.format(
    username='tsmdash',
    password=parse.quote('@75m4dm1n'),
    host='tsmdash.rjo.serpro',
    port='5432',
    database='tsmdash',
  )
)

# PARAMETRIZAÇÃO DA APLICAÇÃO
################################################################
# basedirwin = 'D:\\Git\\IBMEC\\Projeto-DAeA\\Dataset\\CSVS\\' # PC
# fonte = 'D:\\Git\\IBMEC\\Projeto-DAeA\\CSVS\\' # PC
#################################################################
# basedirwin = 'C:\\Git\\Projeto-DAeA\\Dataset\\CSVS\\' #Notebook
# fonte = 'C:\\Git\\Projeto-DAeA\\CSVS\\' # Notebook
#################################################################
basedirwin = '/var/www/html/tsm-dashboard2/backup/' #Trabalho
fonte = '/var/www/html/tsm-dashboard2/backup_fonte/' #Trabalho
#################################################################
warnings.simplefilter(action='ignore', category=FutureWarning)

# REMOVE CSVs VELHOS E COPIA OS NOVOS
if os.path.exists(basedirwin):
    shutil.rmtree(basedirwin)
else:
    sys.exit("Erro ao apagar o diretório de CSVs antigos. Não encontrado.")

try:
    shutil.copytree(fonte, basedirwin, dirs_exist_ok=True)
except OSError as err:
    sys.exit("Erro copiando a pasta de CSVs novos: % s" % err)

# GERANDO LISTA DE PASTAS
try:
    listadir = os.listdir(basedirwin)
except OSError as err:
    if err.errno == errno.ENOENT:
        sys.exit("Erro listando o diretório de CSVs fonte: % s" % err)

# FORMATANDO O ARQUIVO DE PARTIÇÕES
for dir in listadir:
    with open(basedirwin + dir + '/particoes.csv', 'r+') as file:
        espaco = file.readlines()
        for ln in espaco:
            file.seek(espaco.index(ln))
            dir2 = dir[6:8] + dir[4:6] + dir[0:4]
            ln2 = ln[:-1] + "," + dir2 + "\n"
            with open(basedirwin + dir + '/particoes2.csv', 'a') as fileNovo:
                fileNovo.write(ln2)
            fileNovo.close()
    file.close()
    os.remove(basedirwin + dir + '/particoes.csv')
    os.rename(basedirwin + dir + '/particoes2.csv', basedirwin + dir + '/particoes.csv')

# CARREGANDO OS DADOS DE BACKUP NO BANCO DE DADOS
df_bkp = pd.DataFrame()
for dir in listadir:
    df_bkp = df_bkp.append(pd.read_csv(basedirwin + dir + '/coletas.csv', header=None))
df_bkp.columns = ['nodename', 'datainicio', 'status', 'result', 'datafim', 'server']
df_bkp.head(0).to_sql('evnts', engine, if_exists='append',index=False)
conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df_bkp.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'evnts', null="")
conn.commit()
conn.close()

# CARREGANDO OS DADOS DE ESPAÇO EM DISCO DAS PARTIÇÕES NO BANCO DE DADOS
df_vol = pd.DataFrame()
for dir in listadir:
    df_vol = df_vol.append(pd.read_csv(basedirwin + dir + '/particoes.csv', header=None))
df_vol.columns = ['particao', 'total', 'usado', 'livre', 'porcentagem', 'server', 'data']
df_vol.head(0).to_sql('espaco', engine, if_exists='append',index=False)
conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df_vol.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'espaco', null="")
conn.commit()
conn.close()
