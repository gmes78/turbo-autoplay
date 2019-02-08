import pathlib

import pafy

from library import MusicInfo


def download(url: str, download_dir: pathlib.Path):
    video = pafy.new(url)
    stream = video.getbestaudio()
    file_name = video.id + '.' + stream.extension
    path = download_dir.joinpath(file_name)

    stream.download(path)

    return MusicInfo(video.id, video.title, video.length, file_name)
