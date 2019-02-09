import logging
import pathlib

import aiofiles
import aiohttp
import pafy

from library import MusicInfo

logger = logging.getLogger(__name__)

CHUNK_SIZE = 131072  # 128KiB


async def download(session: aiohttp.ClientSession, url: str,
                   download_dir: pathlib.Path):
    video = pafy.new(url)
    stream = video.getbestaudio()
    file_name = video.videoid + '.' + stream.extension
    path = download_dir.joinpath(file_name)

    logger.info('Downloading video {} with URL: {}', video.videoid, stream.url)
    async with session.get(stream.url) as resp:
        if resp.status == 200:
            logger.info('Opening file {}', path)
            async with aiofiles.open(path, 'wb') as file:
                while True:
                    chunk = await resp.content.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    await file.write(chunk)
        else:
            logger.error('Server responded with status {}: {}', resp.status,
                         resp.reason)
            return None

    logger.info('Video {} downloaded successfully', video.videoid)
    return MusicInfo(video.videoid, video.title, video.length, file_name)
