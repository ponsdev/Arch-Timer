import connDB
# import classes

if __name__ == '__main__':
    # SQLITE3
    # if not connDB.checkDB():
    #     db = connDB.connectDB("archtimer")
    #     connDB.criarDBBase(db)
    # else:
    #     db = connDB.connectDB("archtimer")

    # MONGODB
    db = connDB.connectDB("archtimer")

# connDB.criarDBBase(db)
# connDB.addClienteDB(db, 19001, "SM_CRISTAL", "/home/vinicius/dropbox/logs")
# connDB.addClienteDB(db, 19002, "SM_ALMEIDA", "/home/vinicius/dropbox/logs")
# connDB.updateClienteDB(db, 19003, 19001, "SM_CRISTAL",
#                        "/home/vinicius/dropbox/logs")
# connDB.delClienteDB(db, 19002)

# connDB.criarDBCliente(db, 19001)
# connDB.updateNameDBCliente(db, 19003, 19001)
# connDB.delDBCliente(db, 19001)

connDB.addLog(db, 19001, '19001_teste.dwg', 10, 'vinicius')

db.closeDB()
