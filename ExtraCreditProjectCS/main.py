from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.event import EventDispatcher
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem
# from kivy.uix.widget import Widget
# from kivy.properties import StringProperty

from databaseMethods import checkUserName
from databaseMethods import addUser
from databaseMethods import findUser
from databaseMethods import checkPlaylist
from databaseMethods import checkedPlaylist
from databaseMethods import updateEmptyPlaylist
from databaseMethods import convertStrToStrList
from databaseMethods import convertListToStrList
from databaseMethods import updatePlaylist
from databaseMethods import deleteEntirePlaylist
from databaseMethods import insertPlaylist

from circularDoublyLinkedList import Song
from circularDoublyLinkedList import Playlist

from backend import Database

import sqlite3

Builder.load_file('design.kv')


database = Database("database.db")
viewPlaylist = database.view()
GlobalUsername = None
GlobalPlaylist = None
GlobalList = None

##############################################################################################################################
class WelcomeScreen(Screen):
    def log_in_screen(self):
        self.manager.current = "login_screen"

    def sign_up_screen(self):
        self.manager.current = "signup_screen"

##############################################################################################################################
class LoginScreen(Screen):
    def log_in(self, username):
        if checkUserName(username) == True:
            global GlobalUsername
            GlobalUsername = username
            global GlobalPlaylist
            GlobalPlaylist = checkPlaylist(viewPlaylist, GlobalUsername)

            if GlobalPlaylist == None:
                GlobalPlaylist = None
            else:
                listOfSongs = []
                for i in GlobalPlaylist:
                    listOfSongs.append(i.strip('\"'))
                
                GlobalPlaylist = listOfSongs

                global GlobalList

                if GlobalPlaylist == None:
                    return 'No Songs in Playlist'
                else:
                    y = ""
                    index = 0
                    for i in GlobalPlaylist:
                        y += str(index) + i + "\n"
                        index += 1

                    GlobalList = y
            print(GlobalPlaylist, GlobalList)

            self.manager.current = "menu_screen"
        else:
            self.manager.current = "login_error_screen"

    def back_to_welcome(self):
        self.manager.current = "welcome_screen"

class LoginErrorScreen(Screen):
    def back_to_login(self):
        self.manager.current = "login_screen"

##############################################################################################################################
class SignUpScreen(Screen):
    def signup_submit(self, desired_username):
        if checkUserName(desired_username) == False:
            addUser(desired_username)
            self.manager.current = "signup_success_screen"
        else:
            self.manager.current = "signup_error_screen"
        
    def back_to_welcome(self):
        self.manager.current = "welcome_screen"

class SignUpSuccessScreen(Screen):
    def back_to_welcome(self):
        self.manager.current = "welcome_screen" 

class SignUpErrorScreen(Screen):
    def back_to_signup(self):
        self.manager.current = "signup_screen"

##############################################################################################################################
class MenuScreen(Screen):
    def to_create_playlist(self):
        self.manager.current = "create_playlist_screen"

    def to_add_song(self):
        self.manager.current = "add_song_screen"

    def to_update_song(self):
        # global GlobalPlaylist
        # global GlobalList

        # if GlobalPlaylist == None:
        #     return 'No Songs in Playlist'
        # else:
        #     y = ""
        #     index = 0
        #     for i in GlobalPlaylist:
        #         y += str(index) + i + "\n"
        #         index += 1

        #     print('MG',y)
        #     GlobalList = y

        self.manager.current = "update_song_names_screen"

        

    def to_delete_song(self):
        self.manager.current = "delete_songs_screen"

    def to_delete_entire_playlist(self):
        self.manager.current = "delete_entire_playlist_screen"

    def to_view_playlist(self):
        self.manager.current = "view_playlist_screen"

    def logout(self):
        self.manager.current = "welcome_screen"

    # def update_song_list(self):
    #     global GlobalPlaylist

    #     print('MGlobalPlaylist!!!!!!!!!!!!!', GlobalPlaylist)

    #     if GlobalPlaylist == None:
    #         return 'No Songs in Playlist'
    #     else:
    #         y = ""
    #         index = 0
    #         for i in GlobalPlaylist:
    #             y += str(index) + i + "\n"
    #             index += 1

    #         print('MG',y)
    #         return str(y)

##############################################################################################################################
class CreatePlaylistScreen(Screen):        
    def create_playlist_submit(self, name_of_first_song):
        global database
        global GlobalUsername

        if checkedPlaylist(GlobalUsername) == True:
            updateEmptyPlaylist(GlobalUsername, name_of_first_song)
            self.manager.current = "create_playlist_success_screen"
        elif checkedPlaylist(GlobalUsername) == False:
            self.manager.current = "create_playlist_error_screen"

    def back_to_menu(self):
        self.manager.current = "menu_screen"

class CreatePlaylistSuccessScreen(Screen):
    def back_to_menu(self):
        self.manager.current = "menu_screen"

class CreatePlaylistErrorScreen(Screen):
    def back_to_menu(self):
        self.manager.current = "menu_screen"

##############################################################################################################################
class AddSongScreen(Screen):
    def add_song_submit(self, song_title, song_position):
        global GlobalPlaylist
        global GlobalUsername

        checked = checkedPlaylist(GlobalUsername)

        if checked == False:
            updatePlaylist(GlobalUsername, song_title, song_position)
            self.manager.current = "add_song_success_screen"
        elif checked == True:
            self.manager.current = "add_song_error_screen"

    def back_to_menu(self):
        self.manager.current = "menu_screen"

class AddSongSuccessScreen(Screen):
    def back_to_add_song(self):
        self.manager.current = "add_song_screen"

class AddSongErrorScreen(Screen):
    def back_to_add_song(self):
        self.manager.current = "add_song_screen"

##############################################################################################################################
class UpdateSongNamesScreen(Screen):
    def song_list(self):
        global GlobalList

        print('Update:Song List', GlobalList)

        if GlobalList == None:
            return 'No List'
        else:
            return GlobalList

    def update_song_submit(self, number_of_song, new_desired_name):
        global GlobalUsername
        global GlobalPlaylist

        checked = checkedPlaylist(GlobalUsername)

        if checked == False:
            playlist = Playlist()
            playlist.createPlaylist(GlobalPlaylist[0])
            for song in GlobalPlaylist[1:]:
                playlist.insertSong(song, 'E')

            playlist.updateSong(new_desired_name, int(number_of_song))
            x = []
            for node in playlist:
                x.append(node.title)
            
            deleteEntirePlaylist(GlobalUsername)
            insertPlaylist(GlobalUsername, str(x))
            self.manager.current = "update_song_names_success_screen"
        else:
            self.manager.current = "update_song_names_error_screen"

    def back_to_menu(self):
        self.manager.current = "menu_screen"
    
class UpdateSongNamesSuccessScreen(Screen):
    def back_to_update_song(self):
        self.manager.current = "update_song_names_screen"

class UpdateSongNamesErrorScreen(Screen):
    def back_to_update_song(self):
        self.manager.current = "update_song_names_screen"

##############################################################################################################################
class DeleteSongsScreen(Screen):
    def song_list(self):
        global GlobalList

        print('Delete:Song List', GlobalList)

        if GlobalList == None:
            return 'No List'
        else:
            return GlobalList

    def delete_song_submit(self, number_of_delete):
        global GlobalUsername
        global GlobalPlaylist

        checked = checkedPlaylist(GlobalUsername)

        if checked == False:
            playlist = Playlist()
            playlist.createPlaylist(GlobalPlaylist[0])
            for song in GlobalPlaylist[1:]:
                playlist.insertSong(song, 'E')

            playlist.deleteSong(int(number_of_delete))
            x = []
            for node in playlist:
                x.append(node.title)
            
            deleteEntirePlaylist(GlobalUsername)
            insertPlaylist(GlobalUsername, str(x))
            self.manager.current = "delete_songs_success_screen"
        else:
            self.manager.current = "delete_songs_error_screen"

        pass

    def back_to_menu(self):
        self.manager.current = "menu_screen"   

class DeleteSongsSuccessScreen(Screen):
    def back_to_delete_song(self):
        self.manager.current = "delete_songs_screen"

class DeleteSongsErrorScreen(Screen):
    def back_to_delete_song(self):
        self.manager.current = "delete_songs_screen"

##############################################################################################################################
class DeleteEntirePlaylistScreen(Screen):
    def yes(self):
        global GlobalUsername
        global GlobalPlaylist

        checked = checkedPlaylist(GlobalUsername)

        if checked == False:
            deleteEntirePlaylist(GlobalUsername)
            self.manager.current = "delete_entire_playlist_success_screen"
        else:
            self.manager.current = "delete_entire_playlist_error_screen"

    def no(self):
        self.manager.current = "menu_screen"

    def back_to_menu(self):
        self.manager.current = "menu_screen"  

class DeleteEntirePlaylistSuccessScreen(Screen):
    def back_to_menu(self):
        self.manager.current = "menu_screen"  

class DeleteEntirePlaylistErrorScreen(Screen):
    def back_to_menu(self):
        self.manager.current = "menu_screen" 

##############################################################################################################################
class ViewPlaylistScreen(Screen):
    def previous_song(self):
        pass

    def next_song(self):
        pass

    def back_to_menu(self):
        self.manager.current = "menu_screen" 

class ViewPlaylistErrorScreen(Screen):
    def back_to_menu(self):
        self.manager.current = "menu_screen" 

##############################################################################################################################
# class MyClass(EventDispatcher):
#     global GlobalPlaylist
#     global GlobalUsername

#     x = GlobalPlaylist
#     def on_x(self. instance, value):
#         app = App.get_running_app()
#         app. 

class RootWidgit(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidgit()

if __name__ == '__main__':
    MainApp().run()
