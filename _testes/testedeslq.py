import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE Processos(Ano smallint, Nome varchar(255), Municipio varchar(255))"
)

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())

cur.execute('INSERT INTO Processos VALUES (2022, "Fulano da Silva", "Icoaraci"), (2019, "Ciclano da Costa", "Belem")')

