import asyncio
import logging
import pathlib

import aiofiles
import aiohttp
import pafy

from library import MusicInfo, MusicLibrary

logger = logging.getLogger(__name__)

CHUNK_SIZE = 131072  # 128KiB
SLEEP_DELAY = 60


async def download(session: aiohttp.ClientSession, url: str,
                   download_dir: pathlib.Path):
    try:
        video = pafy.new(url)
    except asyncio.CancelledError:
        raise
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
    except asyncio.CancelledError:
        raise
    except Exception as e:
        logger.error(f'Error downloading {stream.url} to file {path}: {e}')
        return

    logger.info(f'Video {video.videoid} downloaded successfully')
    return MusicInfo(video.videoid, video.title, video.length, file_name)


async def download_task(download_path: pathlib.Path,
                        url_list_file: pathlib.Path, library: MusicLibrary,
                        library_lock: asyncio.Lock,
                        library_file: pathlib.Path):
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                with url_list_file.open('r', encoding='utf-8') as file:
                    url = file.readline()

                if url.strip() == '':
                    await asyncio.sleep(SLEEP_DELAY)
                    continue

                music = await download(session, url.strip(), download_path)

                async with library_lock:
                    library.add(music)

                logger.info(f'Added music {music.id} to the library')

                sync_task = asyncio.create_task(
                    library.write_to_file(library_file))

                with url_list_file.open('r+', encoding='utf-8') as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if line != url:
                            file.write(line)
                    file.truncate()
            except asyncio.CancelledError:
                logger.info('Ending YouTube download task')
                return
            except Exception as e:
                logger.error(
                    f'Exception occured while downloading from Youtube: {e}')
