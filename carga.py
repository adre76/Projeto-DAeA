from tkinter import FIRST
from sqlalchemy import create_engine
from urllib import parse
import psycopg2, io, os
import pandas as pd

# Variáveis de ambiente
basedirbkp = "/var/www/html/tsm-dashboard2/backup/"
basedirbkpwin = "C:\\Git\\tsm-dashboard2\\backup\\"
listadir = os.listdir(basedirbkpwin)
df_concat = []

engine = create_engine(
  'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'.format(
    username='tsmdash',
    password=parse.quote('@75m4dm1n'),
    host='tsmdash.rjo.serpro',
    port='5432',
    database='tsmdash',
  )
)

for dir in listadir:
    colunas = ['nodename', 'datainicio', 'status', 'result', 'datafim', 'server']
    df = pd.read_csv(basedirbkpwin + dir + '\\coletas.csv', header=None, names=colunas)
    df_concat.append(df)

    with open(basedirbkpwin + dir + '\\particoes.csv', 'r+') as file:
        espaco = file.readlines()
        for ln in espaco:
            file.seek(espaco.index(ln))
            dir2 = dir[0:4] + "/" + dir[4:6] + "/" + dir[6:8]
            ln2 = ln[:-1] + "," + dir2 + "\n"
            with open(basedirbkpwin + dir + '\\particoes2.csv', 'a') as fileNovo:
                fileNovo.write(ln2)
            fileNovo.close()
    file.close()
    os.remove(basedirbkpwin + dir + '\\particoes.csv')
    os.rename(basedirbkpwin + dir + '\\particoes2.csv', basedirbkpwin + dir + '\\particoes.csv')

big_frame = pd.concat(df_concat, axis=0, ignore_index=True, sort=True)
big_frame.sort_values("nodename", inplace=True)
big_frame.drop_duplicates(keep=FIRST, inplace=True)

big_frame.head(0).to_sql('evnts', engine, if_exists='append',index=False)
conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
big_frame.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'evnts', null="")
conn.commit()
conn.close()

df_concat = []

for dir in listadir:
    colunas = ['particao', 'esp_total', 'esp_usado', 'esp_livre', 'porc_uso', 'server']
    df = pd.read_csv(basedirbkpwin + dir + '\\particoes.csv', header=None, names=colunas)
    df_concat.append(df)

big_frame = pd.concat(df_concat, axis=0, ignore_index=True, sort=True)
big_frame.sort_values("server", inplace=True)
big_frame.drop_duplicates(keep=FIRST, inplace=True)

big_frame.head(0).to_sql('espaco', engine, if_exists='append',index=False)
conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
big_frame.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'espaco', null="")
conn.commit()
conn.close()