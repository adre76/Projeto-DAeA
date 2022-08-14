# IMPORTANDO BIBLIOTECAS
import os, shutil, sys
import errno
import pandas as pd

# DIRETÓRIO BASE DE CSVs
basedirwin = 'D:\\Git\\IBMEC\\Projeto-DAeA\\Dataset\\CSVS\\'

# REMOVE CSVs VELHOS E COPIA OS NOVOS
if os.path.exists(basedirwin):
    shutil.rmtree(basedirwin)
else:
    sys.exit("Erro ao apagar o diretório de CSVs antigos. Não encontrado.")

try:
    shutil.copytree('D:\\Git\\IBMEC\\CSVS', 'D:\\Git\\IBMEC\\Projeto-DAeA\\Dataset\\CSVS\\', dirs_exist_ok=True)
except OSError as err:
    # if err.errno == errno.ENOENT:
    sys.exit("Erro copiando a pasta de CSVs novos: % s" % err)

# VARIÁVEIS DE AMBIENTE
try:
    listadir = os.listdir(basedirwin)
except OSError as err:
    if err.errno == errno.ENOENT:
        sys.exit("Erro listando o diretório de CSVs fonte: % s" % err)

# FORMATANDO O ARQUIVO DE VOLUMES
for dir in listadir:
    with open(basedirwin + dir + '\\particoes.csv', 'r+') as file:
        espaco = file.readlines()
        for ln in espaco:
            file.seek(espaco.index(ln))
            dir2 = dir[0:4] + "/" + dir[4:6] + "/" + dir[6:8]
            ln2 = ln[:-1] + "," + dir2 + "\n"
            with open(basedirwin + dir + '\\particoes2.csv', 'a') as fileNovo:
                fileNovo.write(ln2)
            fileNovo.close()
    file.close()
    os.remove(basedirwin + dir + '\\particoes.csv')
    os.rename(basedirwin + dir + '\\particoes2.csv', basedirwin + dir + '\\particoes.csv')

# CARREGANDO OS DADOS DE BACKUP NO DATASET
df_bkp = pd.DataFrame()
for dir in listadir:
    df_bkp = df_bkp.append(pd.read_csv(basedirwin + dir + '\\coletas.csv', header=None))
df_bkp.columns = ['nodename', 'datainicio', 'status', 'result', 'datafim', 'server']

# CARREGANDO OS DADOS DE VOLUME NO DATASET
df_vol = pd.DataFrame()
for dir in listadir:
    df_vol = df_vol.append(pd.read_csv(basedirwin + dir + '\\particoes.csv', header=None))
df_vol.columns = ['particao', 'total', 'usado', 'livre', 'porcentagem', 'server', 'data']