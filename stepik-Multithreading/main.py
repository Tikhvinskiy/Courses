import logging
from joblib import Parallel, delayed, parallel_config
import multiprocessing
from multiprocessing import Manager, Lock
import concurrent.futures



def log_init(logger,
             log_file_info: str = 'logs_info1.txt', log_file_error: str = 'logs_err1.txt',
             out_stream: bool = 1, out_file_info: bool = 1, out_file_error: bool = 0):
    """ Set logger parameters """

    logger.setLevel(logging.INFO)
    log_formatter = logging.Formatter('{asctime}, {levelname}, {message}', style='{')

    # Вывод в консоль
    if out_stream:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)
        logger.addHandler(stream_handler)

    # INFO Вывод в файл
    if out_file_info:
        file_handler_info = logging.FileHandler(log_file_info, mode='w', encoding='UTF-8')
        file_handler_info.setFormatter(log_formatter)
        file_handler_info.setLevel(logging.INFO)
        logger.addHandler(file_handler_info)

    # ERROR Вывод в файл
    if out_file_error:
        file_handler_error = logging.FileHandler(log_file_error, mode='w', encoding='UTF-8')
        file_handler_error.setFormatter(log_formatter)
        file_handler_error.setLevel(logging.ERROR)
        logger.addHandler(file_handler_error)

    return logger


from process import process


def main():
    a = []
    logger.info('start')
    #with Manager() as manager:
       # global_lock = manager.Lock()
    with concurrent.futures.ProcessPoolExecutor(2) as pool:
        a.append(pool.submit(process, 5, 'global_lock'))
        a.append(pool.submit(process, 8, 'global_lock'))
        a.append(pool.submit(process, 10, 'global_lock'))
        a.append(pool.submit(process, 12, 'global_lock'))

    done, not_done = concurrent.futures.wait(a)

    print(done, not_done)


if __name__ == '__main__':
    logger = logging.getLogger()
    #logger = multiprocessing.get_logger()
    logger = log_init(logger)
    main()
    #print(done, not_done)
