from backend import Database
import json

database = Database("database.db")
viewPlaylist = database.view()

def checkUserName(userName):
    searchForUsername = database.search(userName)

    if len(searchForUsername) > 0:
        return True
    else:
        return False

def addUser(userName):
    database.createUser(userName, None)

def findUser(data, userName):
    for i in data:
        if i[1] == userName:
            return i

def checkPlaylist(playlist, userName):
    checkedUser = findUser(playlist, userName)

    if checkedUser[-1] == None:
        return None
    elif type(checkedUser[-1]) == str:
        listString = checkedUser[-1]
        splicedListString = listString[1:-1]
        listPlaylist = splicedListString.split(', ')
        return listPlaylist

def checkedPlaylist(userName):
    checkedPlaylist = checkPlaylist(viewPlaylist, userName)

    if checkedPlaylist == None:
        return True
    else:
        return False


def updateEmptyPlaylist(userName, playlist):
    id = 0
    for i in viewPlaylist:
        if i[1] == userName:
            id = i[0]

    convert = convertStrToStrList(playlist)

    database.updatePlaylist(id,userName,convert)

def updatePlaylist(username, songTitle, songPosition):
    id = 0
    for i in viewPlaylist:
        if i[1] == username:
            id = i[0]

    oldPlaylist = checkPlaylist(viewPlaylist, username)
    newPlaylist = []
    for i in oldPlaylist:
        newPlaylist.append(i)

    if songPosition == "B":
        newPlaylist.insert(0, songTitle)
    elif songPosition == "E":
        newPlaylist.append(songTitle)

    final = convertListToStrList(newPlaylist)
    final = final.replace("\\", "")

    database.updatePlaylist(id, username, final)

def deleteEntirePlaylist(username):
    id = 0
    for i in viewPlaylist:
        if i[1] == username:
            id = i[0]

    database.updatePlaylist(id, username, None)

def insertPlaylist(username, playlist):
    id = 0
    for i in viewPlaylist:
        if i[1] == username:
            id = i[0]

    database.updatePlaylist(id, username, playlist) 



def convertStrToStrList(string):
    strList = [string]
    return str(strList)

def convertListToStrList(arr):
    return str(arr)

# addUser('Geoffrey')
# addUser('Kobe')
# updateEmptyPlaylist('Geoffrey', 'Song1')
# updateEmptyPlaylist('Kobe', 'Song1')
# print(viewPlaylist)
# print(updatePlaylist('Kobe', 'Song2'))
# # x = viewPlaylist[-1][-1]
# # newx = x.replace("\\", "")
# # print(newx)
# print(viewPlaylist)
# print(viewPlaylist[-1][-1].replace("\\", ""))

# print(checkPlaylist(viewPlaylist, 'Kobe'))
# print(checkedPlaylist('Kobe'))

# updatePlaylist('Geoffrey', 'Song3', 'B')
# updatePlaylist('Kobe', 'Song3', 'E')
# print(viewPlaylist)
# print(checkPlaylist(viewPlaylist, 'Geoffrey'))