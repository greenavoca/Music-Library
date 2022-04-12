import random
import os.path


library = os.path.isfile("music_lib.txt")
if library:
    print("Library exists")
else:
    with open("music_lib.txt", "w"):
        print("Creat library file")


def get_all():
    songs = []
    with open("music_lib.txt", "r") as music:
        if os.path.getsize(library) is not None:
            for song in music:
                author, title, genre = song.strip().split(", ")
                songs.append({
                    "author": author,
                    "title": title,
                    "genre": genre
                })
            return songs
        else:
            print("Empty database")


def show_list(songs):
    print()
    for song in songs:
        print(f"{song['author']} - {song['title']} ({song['genre']})")
    print()


def add():
    author = input("Enter an author: ").strip().lower()
    title = input("Enter a title: ").strip().lower()
    genre = input("Enter a genre: ").strip().lower()
    with open("music_lib.txt", "r") as checker:
        data = checker.read()

    with open("music_lib.txt", "a") as position:
        song = f"{author}, {title}"
        if song not in data:
            position.write(f"{author}, {title}, {genre}" + "\n")
        else:
            print(f"Song already exist!")


def find():
    songs_list = get_all()
    match_songs = []
    word = input("Enter author, title or genre: ").strip().lower()
    for song in songs_list:
        if word in song['author'] or word in song['title'] or word in song['genre']:
            match_songs.append(song)

    return match_songs


def delete():
    if os.path.getsize("music_lib.txt") != 0:    
        delete_list = get_all()
        author = input("Enter author name to delete: ").strip().lower()
        title = input("Enter title to delete: ").strip().lower()
        for song in delete_list:
            if author in song['author'] or title in song['title']:
                if title in song['author'] or title in song['title']:
                    delete_list.remove(song)

        with open("music_lib.txt", "w") as file:
            for each in delete_list:
                auth, tit, gen = each['author'], each['title'], each['genre']
                file.write(f"{auth}, {tit}, {gen}" + "\n")
    else:
        print(f"First add a song!")


def random_song():
    songs_list = get_all()
    if songs_list:
        song = random.choice(songs_list)
        print(f"Your random song is: {song['author']} - {song['title']} ({song['genre']})")
    else:
        print("Database is empty")


menu = """
WELCOME IN YOUR MUSIC LIBRARY!

Please choose what would you like to do:
    
    (s) - show your library
    (f) - find song
    (a) - add song
    (d) - delete song
    (r) - get random song
    (q) - quit

"""

def main():
    choose = input(menu).strip().lower()

    while choose != "q":
        if choose == "s":
            music_list = get_all()
            show_list(music_list)
        elif choose == "f":
            matching_songs = find()
            if matching_songs:
                show_list(matching_songs)
            else:
                print(f"It's empty :(")
        elif choose == "a":
            add()
        elif choose == "d":
            delete()
        elif choose == "r":
            random_song()
        else:
            print(f"There is no {choose} choice!")

        choose = input(menu).strip().lower()


if __name__ == "__main__":
    main()
    print(f"See you again!")
