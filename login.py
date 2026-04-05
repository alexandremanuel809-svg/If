import mysql.connector

 # Estabelecer conexão  

try:
    cnx=mysql.connector.connect(
     host="127.0.0.1",
     user="root",
     password="root",
     database="Login",
     port="3306"

 )

    # Criar cursor para executar comandos
    cursor=cnx.cursor()

    mail=str(input("Digite o seu email: "))
    passe=str(input("Digite a sua senha: "))
    print ("Bem vindo")

    query_Insert = (f"""INSERT INTO `informacoes` 
                    (`email`, `senha`)
                    VALUES
                    ('{mail}', '{passe}');""")

    # Executar um comando SQL
    cursor.execute(query_Insert)
    cnx.commit()

    query_select=("SELECT * FROM informacoes")
    cursor.execute(query_select)

    for row in cursor:
        print (row)

except mysql.connector.Error as error:
    print (f"Error:{error}") 

finally:
    if "cursor" in locals()  and cursor is not None:
        cursor.close()
    if "cnx" in locals() and cnx is not None:
        cnx.close()
print ("Voce foi cadastrado")

   