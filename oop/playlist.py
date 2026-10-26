class Song:
  def __init__(self, title: str, artist: str):
    if not title.strip():
      raise ValueError("Название песни не может быть пустым")

    if not artist.strip():
      raise ValueError("Исполнитель не может быть пустым")

    self.title = title
    self.artist = artist

  def __str__(self):
    return f"{self.title} - {self.artist}"

class Playlist:
  def __init__(self, name: str):
    self.name = name
    self.__songs: list[Song] = []

  def add_song(self, title: str, artist: str):
    song = Song(title, artist)
    self.__songs.append(song)

    print(f"Песня добавлена: {song}")

  def remove_song(self, title: str):
    for song in self.__songs:
      if song.title.lower() == title.lower():
        self.__songs.remove(song)
        print(f"Песня удалена: {song}")
        return

    print("Такой песни нет")

  def show_songs(self):
    print(f"Плейлист: {self.name}")

    if not self.__songs:
      print("Плейлист пуст")
      return

    for song in self.__songs:
      print(song)

  def get_count(self):
    return len(self.__songs)

playlist = Playlist("My Playlist")
playlist.add_song("Song 1", "Artist 1")

print(playlist.get_count())

playlist.show_songs()
playlist.remove_song("Song 1")
playlist.show_songs()