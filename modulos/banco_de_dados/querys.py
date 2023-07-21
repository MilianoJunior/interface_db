from modulos.banco_de_dados.variaveis import config_table

def creat_insert(table):
    query = f'INSERT INTO {table} ('
    values = ''
    cont = 1
    for key, value in config_table[table].items():
        if not 'ug0' in key:
            continue
        query += f'{key},\n '
        values += "'${" + str(cont) + "}',\n"
        cont += 1

    query += ') \n VALUES ('
    query += values
    query += ');'
    print(query)