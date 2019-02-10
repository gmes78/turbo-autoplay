import asyncio
import logging
import pathlib

import vlc

logger = logging.getLogger(__name__)
SLEEP_DELAY = 3
INITIAL_WAIT = 5


class Player:
    def __init__(self):
        self.vlc_instance = vlc.Instance()
        if self.vlc_instance is None:
            raise Exception('Failed to initialize VLC instance')

        self.mediaplayer = vlc.MediaPlayer(self.vlc_instance)
        if self.mediaplayer is None:
            raise Exception('Failed to initialize VLC MediaPlayer')

    async def play(self, path: str):
        logger.info(f'Playing file {path}')

        media = self.mediaplayer.set_mrl(path)
        if media is None:
            logger.error(f'Failed to get Media for {path}')
            return

        result = self.mediaplayer.play()
        if result == -1:
            logger.error(
                f'Failed to play {path}: MediaPlayer.play() returned -1')
            return

        # We need to wait because it doesn't start playing immediately
        await asyncio.sleep(INITIAL_WAIT)
        while self.mediaplayer.is_playing():
            await asyncio.sleep(SLEEP_DELAY)

        logger.info(f'Finished playing file {path}')
