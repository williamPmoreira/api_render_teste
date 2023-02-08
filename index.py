#pip install mysql-connector-python
#pip install flask
#pip install myapp

import mysql.connector
from datetime import datetime
from flask import Flask, make_response, jsonify, request



#conexão com banco de dados
mydb = mysql.connector.connect(
    # Dados de conexão
    host = "localhost",   #endereço_da_instância_RDS
    user = "root",          #nome_de_usuario'
    password = "#Nitro10#",  #senha
    database = "sys"         #nome_do_banco_de_dados
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def home():
    return "API funcionando!"

@app.route('/geracao', methods=['GET'])
def geracao():

    sql_1 = f"SELECT dataHora, usinaUhe, numUg1, ug1 FROM UHE1 WHERE dataHora BETWEEN '2023-01-01 00:00:00' AND '2023-01-01 03:00:00'"
    sql_2 = f"SELECT dataHora, usinaUhe, numUg2, ug2 FROM UHE1 WHERE dataHora BETWEEN '2023-01-01 00:00:00' AND '2023-01-01 03:00:00'"

    my_cursor = mydb.cursor()
    my_cursor.execute(sql_1)
    scl1 = my_cursor.fetchall()


    ug1 = list()
    for usina in scl1:


        ug1.append(
                    {
                        "data": usina[0],
                        "usina": usina[1],
                        "ug": usina[2],
                        "valor": usina[3]
                    }        
                    )


    my_cursor = mydb.cursor()
    my_cursor.execute(sql_2)
    scl2 = my_cursor.fetchall()

    print (scl2)

    ug2 = list()
    for usina2 in scl2:
        ug2.append(
                    {
                    
                    "data": usina2[0],    
                    "usina": usina2[1],
                    "ug": usina2[2],
                    "valor": usina2[3]
                    }        
                    )

    return make_response(
        jsonify(
                ug1,
                ug2
                )

    )





app.run()
