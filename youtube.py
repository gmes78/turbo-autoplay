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
    try:
        video = pafy.new(url)
    except Exception as e:
        logger.error(f'Failed to get video info: {e}')
        return

    stream = video.getbestaudio(ftypestrict=False)
    if stream is None:
        logger.error(f'Video {video.videoid} does not have any audio streams')
        return

    file_name = video.videoid + '.' + stream.extension
    path = download_dir.joinpath(file_name)

    logger.info(f'Downloading video {video.videoid} with URL: {stream.url}')
    try:
        async with session.get(stream.url) as resp:
            if resp.status == 200:
                logger.info(f'Opening file {path}')
                async with aiofiles.open(path, 'wb') as file:
                    while True:
                        chunk = await resp.content.read(CHUNK_SIZE)
                        if not chunk:
                            break
                        await file.write(chunk)
            else:
                logger.error(f'Server responded with status {resp.status}: '
                             '{resp.reason}')
                return
    except Exception as e:
        logger.error(f'Error downloading {stream.url} to file {path}: {e}')
        return

    logger.info(f'Video {video.videoid} downloaded successfully')
    return MusicInfo(video.videoid, video.title, video.length, file_name)
