class Song:
    def __init__(self, title=None):
        self.title = title
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createPlaylist(self, songTitle):
        newSong = Song(songTitle)
        self.head = newSong
        self.tail = newSong
        newSong.next = newSong
        newSong.prev = newSong
        return "Your playlist has been successfully created!"

    def insertSong(self, songTitle, location):
        if self.head is None:
            return "You have not created a playlist."
        else:
            newSong = Song(songTitle)
            if location == 'B':
                newSong.next = self.head
                newSong.prev = self.tail
                self.head.prev = newSong
                self.head = newSong
                self.tail.next = newSong
            elif location == 'E':
                newSong.next = self.head
                newSong.prev = self.tail
                self.head.prev = newSong
                self.tail.next = newSong
                self.tail = newSong
        return f"{songTitle} has been successfully added to playlist!"

    def deleteSong(self, location):
        if self.head is None:
            return "You have not created a playlist."
        else:
            if location == 000:
                if self.head == self.tail:
                    songTitle = self.head.title
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                    print(f"{songTitle} has been successfully deleted!")
                else:
                    songTitle = self.head.title
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                    print(f"{songTitle} has been successfully deleted!")
            elif location == 999:
                if self.head == self.tail:
                    songTitle = self.head.title
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                    print(f"{songTitle} has been successfully deleted!")
                else:
                    songTitle = self.tail.title
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                    print(f"{songTitle} has been successfully deleted!")
            else:
                tempNode = self.head
                index = 1
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                songTitle = tempNode.next.title
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
                print(f"{songTitle} has been successfully deleted!")

    def deleteEntirePlaylist(self):
        if self.head is None:
            print("There is no playlist to delete.")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("Your playlist has been successfully deleted!")

    def traversePlaylist(self):
        if self.head is None:
            print("There is no playlist to traverse.")
        else:
            tempNode = self.head
            terminate = False
            print('First Song:', tempNode.title)
            while tempNode and terminate == False:
                direction = input('\nNext Song (N)\nPrevious Song (P)\nEnd Viewing (E)?: ')

                if direction == 'N':
                    print(tempNode.next.title)
                    tempNode = tempNode.next

                if direction == 'P':
                    print(tempNode.prev.title)
                    tempNode = tempNode.prev

                if direction == 'E':
                    terminate = True
                
    def updateSong(self, updatedTitle, location):
        if self.head is None:
            print("There are no songs to update")
        else:
            if location == 000:
                songTitle = self.head.title
                self.head.title = updatedTitle
                print(f"{songTitle} has been successfully updated to {updatedTitle}!")
            elif location == 999:
                songTitle = self.tail.title
                self.tail.title = updatedTitle
                print(f"{songTitle} has been successfully updated to {updatedTitle}!")
            else:
                tempNode = self.head
                index = 1
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                songTitle = tempNode.next.title
                tempNode.next.title = updatedTitle
                print(f"{songTitle} has been successfully updated to {updatedTitle}!")

    @staticmethod
    def strToObj(string):
        playlist = Playlist()
        playlist.createPlaylist('None')
        for i in string:
            if i != ',':
                playlist.insertSong(i, 'E')
        return playlist


    def __repr__(self):
        return " "





# playlist = Playlist()
# playlist.createPlaylist('0')

# print(playlist.insertSong('1', 'E'))
# print(playlist.insertSong('2', 'E'))
# playlist.insertSong('3', 'E')

# print([node.title for node in playlist])

# print(playlist.traversePlaylist())


# print([node.title for node in playlist])
# playlist.deleteSong('B')
# print(playlist.deleteSong('E'))
# print([node.title for node in playlist])
# playlist.deleteEntirePlaylist()
# print([node.title for node in playlist])