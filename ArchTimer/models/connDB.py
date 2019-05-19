import psycopg2
import os
import datetime


class connectDB():

    def __init__(self, db_name):
        try:
            # POSTGRES
            self.conn = psycopg2.connect(
                host='localhost', database='archtimer', user='postgres', password='admin')
            self.cursor = self.conn.cursor()
            print('---------------------------------------')
            print("Conectado ao bando de dados!")
            print('---------------------------------------')
        except (Exception, psycopg2.Error):
            print('---------------------------------------')
            print('Falha ao abrir o banco de dados')
            print('---------------------------------------')
            return False

    def closeDB(self):
        if self.conn:
            self.conn.close()
            print('---------------------------------------')
            print('Conexão com o banco de dados encerrada.')
            print('---------------------------------------')


def criarDBBase(db):
    db.cursor.execute("""
    CREATE TABLE clients (
        CodCliente INT PRIMARY KEY NOT NULL,
        Nome TEXT NOT NULL,
        Path TEXT NOT NULL
    );
    """)
    db.conn.commit()
    print("Tabela de clientes criada com sucesso!")

# CLIENTES


def addClienteDB(db, codCliente, nome, path):
    db.cursor.execute("""
    INSERT INTO clients (CodCliente, Nome, Path)
    VALUES (%s,%s,%s)
    """, (codCliente, nome, path))
    db.conn.commit()
    print("Cliente %s adicionado a tabela de clientes!" % nome)


def criarDBCliente(db, codCliente):
    db.cursor.execute("""
    CREATE TABLE logs_""" + str(codCliente) + """ (
        CodUso SERIAL NOT NULL PRIMARY KEY,
        Filename TEXT NOT NULL,
        Date DATE NOT NULL,
        Time DECIMAL(15,2) NOT NULL
    );
    """)
    db.conn.commit()
    print("Tabela CLIENTE: " + str(codCliente) + " criada com sucesso!")


def updateClienteDB(db, old_codCliente, codCliente, nome, path):
    db.cursor.execute("""
    UPDATE clients SET CodCliente = '%d', Nome = '%s', Path  = '%s'
    WHERE CodCliente = '%d' """ % (codCliente, nome, path, old_codCliente))
    db.conn.commit()


def delClienteDB(db, codCliente):
    db.cursor.execute("""
    DELETE FROM clients WHERE CodCliente = '%d'""" % (codCliente))
    db.conn.commit()
    print("Cliente %d apagado!" % (codCliente))


def delDBCliente(db, codCliente):
    db.cursor.execute("""DROP TABLE logs_%d""" % (codCliente))
    print("Tabela do cliente %d foi apagada!" % (codCliente))
    db.conn.commit()


def updateNameDBCliente(db, old_codCliente, codCliente):
    db.cursor.execute("""ALTER TABLE logs_%d RENAME TO logs_%d
    """ % (old_codCliente, codCliente))
    db.conn.commit()

# LOGS


def addLog(db, codCliente, filename, timeInc):
    now = datetime.datetime.now()
    day = int(now.day)
    month = int(now.month)
    year = int(now.year)

    db.cursor.execute("""SELECT * FROM logs_""" + str(codCliente) + """
    WHERE Date = DATE('now') AND Filename = '%s' """ %
                      (str(filename)))

    src = db.cursor.fetchall()
    print(src)
    if (len(src) == 0):
        db.cursor.execute(f"""
        INSERT INTO logs_{codCliente} (Filename, Date, Time)
        VALUES ('%s', DATE('now'), %s);
        """ % (filename, timeInc))
        db.conn.commit()
    else:
        time = src[0][3] + timeInc
        db.cursor.execute(f"""
        UPDATE logs_{codCliente} SET Time = {time}
        WHERE Date = DATE('now') AND Filename = '{filename}' """)
        db.conn.commit()
        print(time)
