# from circularDoublyLinkedList import Playlist
# from databaseMethods import checkUserName
# from databaseMethods import addUser
# from databaseMethods import checkedPlaylist
# from databaseMethods import updatePlaylist
# from backend import Database

# terminate = False
# playlist = None

# userName = input("                   Login\n---------------------------------------------\nEnter your name: ")
# print(checkUserName(userName))

# if checkUserName(userName) == "You do not have an account. Please make an account to start making a playlist!":
#     userInput = input("\nWould you like to make an account (Y/N)?:")
    
#     if userInput == 'Y':
#         desiredUserName = input("\nGreat!\nWhat would you like your user name to be?:")
#         addUser(desiredUserName)
#         print(f"\nThank you {desiredUserName} for creating an account with CRUD CDLL Playlist!\nPlease Login again.")
#         terminate = True
#     elif userInput == 'N':
#         print("\nSorry to hear that. Hopefully you reconsider. Have a good day!")
#         terminate = True
#     else:
#         print(f'\n{userInput} is not a valid command. Please type Y or N.')
#         terminate = True

# while not terminate:
#     try:
#         print(f"\nWelcome to CRUD CDLL Playlist!\nWhat would you like to do today?")
#         direction = input("\n\n            MENU\n-----------------------------\nCreate a playlist (C)\nView playlist (V)\nAdd a song to playlist (A)\nUpdate a song (U)\nDelete a song (D)\nDelete entire playlist (DE)\nTerminate program (T)\nInput:  ")

#         if direction == 'C':
#             if checkedPlaylist(userName) == True:
#                 playlist = Playlist()
#                 songTitle = input("\nWhat is the name of the first song you wish to add?: ")
#                 print(playlist.createPlaylist(songTitle))
#             elif checkedPlaylist(userName) == "You already have a playlist created!":
#                 print(checkedPlaylist(userName))

#         if direction == 'A':
#             songTitle = input("\nWhat is the title of the song you wish to add?: ")
#             extraDirection = input("Would you like to add song to beginning (B) or end (E) of playlist?: ")
#             print(playlist.insertSong(songTitle, extraDirection))
#             # memoryAddress = id(playlist)
#             # print('ctypes!!!!!', ctypes.cast(memoryAddress, ctypes.py_object).value)
#             # print(updatePlaylist(userName, playlist))
            

#         if direction == "U":
#             print("\nList of songs in playlist\n--------------------------")
#             index = 1
#             for song in playlist:
#                 print(index , song.title)
#                 index += 1

#             location = input("\nWhich song would you like to update?\nFirst Song (000)\nLast Song (999)\nOther Song (input number of corresponding song)\nInput: ")
#             songTitle = input("\nWhat would you like to rename the song to?: ")
#             print(playlist.updateSong(songTitle, int(location)))

#         if direction == 'D':
#             print("\nList of songs in playlist\n--------------------------")
#             index = 1
#             for song in playlist:
#                 print(index , song.title)
#                 index += 1

#             extraDirection = input("\nWould you like to delete first song (000), last song (999), or middle (input number of corresponding song): ")
#             print(playlist.deleteSong(int(extraDirection)))

#         if direction == 'V':
#             print(playlist.traversePlaylist())

#         if direction == 'DE':
#             print(playlist.deleteEntirePlaylist())

#         if direction == 'T':
#             print("\nThanks again for using CRUD CDLL Playlist!")
#             terminate = True

#         if direction not in ['C','A','U','D','V','DE','T']:
#             print(f'\n{direction} is not a valid command!\nRefer to Menu for valid commands.')

#     except (AttributeError , TypeError) as e:
#         print('You must first create a playlist before you execute any other commands!')