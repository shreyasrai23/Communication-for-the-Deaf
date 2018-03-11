import sqlite3

c = sqlite3.connect("test.db")
cor = c.cursor()
cor.execute("select * from data")
li = cor.fetchall()
def newRow(name, a):
    c = sqlite3.connect("test.db")
    cor = c.cursor()
    cor.execute("INSERT INTO data VALUES (?,?)", (name, a))
    cor.close()


# Create table


#Insert a row of data


# Save (commit) the changes
c.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
cor.close()

#for x in range(1, 10):
newRow('Shreyas', 'Yes')
newRow('Vivek', 'No')


