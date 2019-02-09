import argparse
import logging
import pathlib

from library import MusicLibrary

log_format = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logger = logging.getLogger(__name__)


class Settings:
    def __init__(self, library_path: pathlib.Path, log_level):
        self.library_path = library_path
        self.log_level = log_level


def parse_arguments():
    parser = argparse.ArgumentParser(description='Music player')
    parser.add_argument('library_path', nargs='?')
    parser.add_argument('-l', '--loglevel', required=False, metavar='LEVEL',
                        dest='log_level', choices=['critical', 'error',
                                                   'warning', 'info', 'debug'])

    args = parser.parse_args()

    if args.library_path:
        library_path = pathlib.Path(args.library_path)
    else:
        library_path = pathlib.Path.cwd()

    if args.log_level == 'critical':
        log_level = logging.CRITICAL
    elif args.log_level == 'error':
        log_level = logging.ERROR
    elif args.log_level == 'warning':
        log_level = logging.WARNING
    elif args.log_level == 'debug':
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    return Settings(library_path, log_level)


def setup_logging(log_file: pathlib.Path, log_level):
    logging.basicConfig(filename=log_file, format=log_format, level=log_level)


def load_library(library_file: pathlib.Path):
    if library_file.is_file():
        logger.info('Found library file, loading')
        try:
            with library_file.open('r', encoding='utf-8') as file:
                return MusicLibrary.from_json(file.read())
        except Exception as e:
            logger.critical('Failed to import library from file:', e)
            raise e
    else:
        logger.warning('Library file not found, using empty library')
        return MusicLibrary()


def main(settings: Settings):
    if not settings.library_path.is_dir():
        settings.library_path.mkdir(parents=True)

    log_file = settings.library_path.joinpath('log.txt')
    setup_logging(log_file, settings.log_level)

    logger.info('Starting')

    library_file = settings.library_path.joinpath('library.json')
    library = load_library(library_file)

    logger.info('Library loaded successfully')


if __name__ == '__main__':
    main(parse_arguments())
