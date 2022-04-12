import random
import os.path


LIBRARY_NAME = 'music_lib.txt'


is_library = os.path.isfile(LIBRARY_NAME)
if not is_library:
    with open(LIBRARY_NAME, "w"):
        print("Create library file")
else:
    print("Library exists", end='\n')


def get_all() -> list:
    songs = []
    with open(LIBRARY_NAME, "r") as music:
        if os.path.getsize(LIBRARY_NAME) is not None:
            for song in music:
                author, title, genre = song.strip().split(", ")
                songs.append({
                    "author": author,
                    "title": title,
                    "genre": genre
                })
            return songs
        else:
            print("Empty database", end='\n')


def show_list(songs_list):
    if not songs_list:
        print("Database is empty", end='\n')
    else:
        for song in songs_list:
            print(f"{song['author']} - {song['title']} ({song['genre']})", end='\n')


def add():
    author = input("Enter an author: ").strip().lower()
    title = input("Enter a title: ").strip().lower()
    genre = input("Enter a genre: ").strip().lower()
    with open(LIBRARY_NAME, "r") as checker:
        data = checker.read()

    with open(LIBRARY_NAME, "a") as position:
        song = f"{author}, {title}"
        if song not in data:
            position.write(f"{author}, {title}, {genre}" + "\n")
        else:
            print(f"Song already exist!")


def find() -> list:
    songs_list = get_all()
    match_songs = []
    word = input("Enter author, title or genre: ").strip().lower()
    for song in songs_list:
        if word in song['author'] or word in song['title'] or word in song['genre']:
            match_songs.append(song)

    return match_songs


def delete():
    if os.path.getsize(LIBRARY_NAME) != 0:
        author = input("Enter author name to delete: ").strip().lower()
        title = input("Enter title to delete: ").strip().lower()
        with open(LIBRARY_NAME, "r") as deleter:
            lines = deleter.readlines()

        with open(LIBRARY_NAME, "w") as file:
            for each in lines:
                if f"{author}, {title}" not in each:
                    file.write(each)
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
            db = get_all()
            show_list(db)
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
            print(f"There is no `{choose}` choice!")

        choose = input(menu).strip().lower()


if __name__ == "__main__":
    main()
    print(f"See you again!")
