import random


class MusicInfo:
    def __init__(self, video_id, title, length, file_name):
        self.id = video_id
        self.title = title
        self.length = length
        self.file_name = file_name


class MusicLibrary:
    def __init__(self):
        self.musics = []

    def add(self, music: MusicInfo):
        self.musics.append(music)

    def get(self, video_id: str):
        for music in self.musics:
            if music.id == video_id:
                return music

    def get_random(self):
        random.choice(self.musics)

    def get_random_with_max_len(self, max_length: int):
        eligible_musics = [m for m in self.musics if m.length <= max_length]
        random.choice(eligible_musics)


