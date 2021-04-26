import sqlite3
from circularDoublyLinkedList import Playlist

class Database:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cdll (id INTEGER PRIMARY KEY, username text, playlist text)")
        self. conn.commit()

    def createUser(self, user, playlist):
        self.cur.execute("INSERT INTO cdll VALUES (NULL, ?, ?)", (user, playlist))
        self.conn.commit()

    def updatePlaylist(self, id, user, playlist):
        self.cur.execute("INSERT OR REPLACE INTO cdll(id, username, playlist) VALUES(?,?,?)", (id,user,playlist))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM cdll")
        rows=self.cur.fetchall()
        return rows

    def search(self,username="",playlist=""):
        self.cur.execute("SELECT * FROM cdll WHERE username=? OR playlist=?", (username,playlist))
        rows=self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()



# songs = ['Song1', 'Song2', 'Song3']
# songs = str(songs)
# playlist = Playlist()
# database = Database("database.db")

# # database.createUser('Geoffrey', songs)
# # database.createUser('Bobby', None)
# viewPlaylist = database.view()
# # print(viewPlaylist)

# def findUser(data, userName):
#     for i in data:
#         if i[1] == userName:
#             return i

# def checkPlaylist(playlist, userName):
#     checkedUser = findUser(playlist, userName)

#     if checkedUser[-1] == None:
#         return "NO PLAYLIST"
#     elif type(checkedUser[-1]) == str:
#         listString = checkedUser[-1]
#         splicedListString = listString[1:-1]
#         listPlaylist = splicedListString.split(', ')
#         return listPlaylist

# checked = checkPlaylist(viewPlaylist, 'Geoffrey')

# if checked != "NO PLAYLIST":
#     playlist.createPlaylist(checked[0])
#     checked.pop(0)
#     for i in checked:
#         playlist.insertSong(i, 'E')

