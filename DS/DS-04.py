"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Data Structure Homework 4
"""
class Song:
    def __init__(self):
        self.title = ''
        self.artist = ''

    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")

    def display(self):
        print(f"{self.title} by {self.artist}")

def main():
    playlist = []
    cmd = 0

    while cmd != 4:
        song = Song()
        cmd = int(input("""Options:
1. Add a new song to the end of the playlist
2. Insert a new song to the beginning of the playlist
3. Play the next song
4. Quit
Enter selection: """))
        if cmd != 4:
            if cmd == 1:
                playlist.append(song.prompt())
            elif cmd == 2:
                playlist.appendleft(song.prompt())
            elif cmd == 3:
                if len(playlist) != 0:
                    print("Playing song:")
                    for i in playlist:
                        i.display()
                else:
                    print("The playlist is currently empty.")
    print("Goodbye")

if __name__ == "__main__":
  main()
