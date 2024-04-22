import os
import sqlite3


class ConnectDB:
    def __init__(self, filename: str):
        self.filename = filename
        self.path = "db/"
        self.extension = ".db"
        

    def GetChatsFileNames(extension: str) -> list:
        fileNamesList = []
        for el in os.listdir("db/"):
            if el.endswith(extension):
                fileNamesList.append(el)
        return fileNamesList
    
    def GetChatsNames(extension: str) -> list:
        namesList = []
        for el in os.listdir("db/"):
            if el.endswith(extension):
                namesList.append(el[:len(el)-len(extension):])
        return namesList
    