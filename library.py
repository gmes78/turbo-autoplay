import json
import random


class MusicInfo:
    def __init__(self, video_id: str, title: str, length: int, file_name: str):
        self.id = video_id
        self.title = title
        self.length = length
        self.file_name = file_name


class MusicInfoEncoder(json.JSONEncoder):
    def default(self, o: MusicInfo):
        return {'file_name': o.file_name, 'id': o.id, 'length': o.length,
                'title': o.title}


class MusicLibrary:
    def __init__(self, musics: [MusicInfo] = []):
        self.musics = musics

    def add(self, music: MusicInfo):
        self.musics.append(music)

    def get(self, video_id: str):
        for music in self.musics:
            if music.id == video_id:
                return music

    def get_random(self):
        return random.choice(self.musics)

    def get_random_with_max_len(self, max_length: int):
        eligible_musics = [m for m in self.musics if m.length <= max_length]
        return random.choice(eligible_musics)

    def into_json(self, pretty=True):
        if pretty:
            return MusicInfoEncoder(indent=4).encode(self.musics)
        else:
            return MusicInfoEncoder().encode(self.musics)

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        musics = [
            MusicInfo(o['id'], o['title'], o['length'], o['file_name'])
            for o in data]
        return MusicLibrary(musics)
