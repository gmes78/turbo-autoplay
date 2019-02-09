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
        logger.error('Failed to get video info: {}', e)
        return

    stream = video.getbestaudio(ftypestrict=False)
    if stream is None:
        logger.error('Video {} does not have any audio streams', video.videoid)
        return

    file_name = video.videoid + '.' + stream.extension
    path = download_dir.joinpath(file_name)

    logger.info('Downloading video {} with URL: {}', video.videoid, stream.url)
    try:
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
                logger.error('Server responded with status {}: {}',
                             resp.status, resp.reason)
                return
    except Exception as e:
        logger.error('Error downloading {} to file {}: {}',
                     stream.url, path, e)
        return

    logger.info('Video {} downloaded successfully', video.videoid)
    return MusicInfo(video.videoid, video.title, video.length, file_name)
