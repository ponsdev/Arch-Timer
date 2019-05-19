import pymongo
import sqlite3
import os
import datetime
import json


class connectDB():

    def __init__(self, db_name):
        try:
            # SQLITE3
            # self.conn = sqlite3.connect("database.db")
            # self.cursor = self.conn.cursor()

            # MONGODB
            maxSevSelDelay = 10
            self.client = pymongo.MongoClient('localhost', 27017,
                                              serverSelectionTimeoutMS=maxSevSelDelay)
            self.db = self.client['archtimer']
            self.client.server_info()

        except pymongo.errors.ServerSelectionTimeoutError:
            print('---------------------------------------')
            print('Falha ao abrir o banco de dados')
            print('---------------------------------------')
            quit()

        print('---------------------------------------')
        print("Conectado ao bando de dados!")
        print('---------------------------------------')

    def closeDB(self):
        if self.client:
            self.client.close()
            print('---------------------------------------')
            print('Conexão com o banco de dados encerrada.')
            print('---------------------------------------')


# def criarDBBase(db):
#     # SQLITE3
#     # db.cursor.execute("""
#     # CREATE TABLE clients (
#     #     CodCliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     #     Nome TEXT NOT NULL,
#     #     Path STRING NOT NULL
#     # );
#     # """)
#     # print("Tabela de clientes criada com sucesso!")

#     # MONGODB
#     # nothing

#     # CLIENTES


def addClienteDB(db, codCliente, nome, path):
    # SQLITE3
    # db.cursor.execute("""
    # INSERT INTO clients (CodCliente, Nome, Path)
    # VALUES (?,?,?)
    # """, (codCliente, nome, path))
    # db.conn.commit()

    # MONGODB
    clientesCol = db.db['clients']
    data = {
        '_id': codCliente,
        'Name': nome,
        'Path': path
    }
    clientesCol.insert_one(data)

    print("Cliente %s adicionado a tabela de clientes!" % nome)


# def criarDBCliente(db, codCliente):
#     db.cursor.execute("""
#     CREATE TABLE logs_""" + str(codCliente) + """ (
#         CodUso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         Filename STRING NOT NULL,
#         Date DATE NOT NULL,
#         Time DECIMAL(15,2) NOT NULL
#     );
#     """)
#     print("Tabela CLIENTE: " + str(codCliente) + " criada com sucesso!")


def updateClienteDB(db, old_codCliente, codCliente, nome, path):
    # SQLITE3
    # db.cursor.execute("""
    # UPDATE clients SET CodCliente = '%d', Nome = '%s', Path  = '%s'
    # WHERE CodCliente = '%d' """ % (codCliente, nome, path, old_codCliente))
    # db.conn.commit()

    # MONGODB
    criteria = db.db.clients.find_one({"_id": old_codCliente})
    data = {
        '_id': codCliente,
        'Name': nome,
        'Path': path
    }
    db.db.clients.update(criteria, data)


def delClienteDB(db, codCliente):
    db.cursor.execute("""
    DELETE FROM clients WHERE CodCliente = '%d'""" % (codCliente))
    db.conn.commit()
    print("Cliente %d apagado!" % (codCliente))


def delDBCliente(db, codCliente):
    db.cursor.execute("""DROP TABLE logs_%d""" % (codCliente))
    print("Tabela do cliente %d foi apagada!" % (codCliente))


def updateNameDBCliente(db, old_codCliente, codCliente):
    db.cursor.execute("""ALTER TABLE logs_%d RENAME TO files_%d
    """ % (old_codCliente, codCliente))

# LOGS


def addLog(db, codCliente, filename, timeInc):
    now = datetime.datetime.now()
    day = int(now.day)
    month = int(now.month)
    year = int(now.year)

    db.cursor.execute("""SELECT * FROM logs_%d
    WHERE Date = DATE('now') AND Filename = '%s' """ %
                      (codCliente, str(filename)))

    src = db.cursor.fetchall()
    print(src)
    if (len(src) == 0):
        db.cursor.execute(f"""
        INSERT INTO logs_{codCliente} (Filename, Date, Time)
        VALUES (?, DATE('now'), ?);
        """, (str(filename), timeInc))
        db.conn.commit()
    else:
        time = src[0][3] + timeInc
        db.cursor.execute(f"""
        UPDATE logs_{codCliente} SET Time = {time}
        WHERE Date = DATE('now') AND Filename = '{filename}' """)
        db.conn.commit()
        print(time)