def process(n, l):

    import logging
    from joblib import Parallel, delayed, parallel_config
    import multiprocessing
    import concurrent.futures


    def get_coin_data(coin, interval, i, l):
        print('111111111111111')
        #logger.info(f"inner")
        if i == 8:
            #logger.error(f"ERROR")
            raise Exception('!!!!')
        return i**i

    #logger = multiprocessing.get_logger()


    #def log_init(logger: multiprocessing.get_logger = logger,
                #log_file_info: str = 'logs_info.txt', log_file_error: str = 'logs_err.txt',
                #out_stream: bool = 1, out_file_info: bool = 0, out_file_error: bool = 0) -> multiprocessing.get_logger:
        ##""" Set logger parameters """

        #logger.setLevel(logging.INFO)
        #log_formatter = logging.Formatter('{asctime}, {message}', style='{')

        ### Вывод в консоль
        #if out_stream:
            #stream_handler = logging.StreamHandler()
            #stream_handler.setFormatter(log_formatter)
            #logger.addHandler(stream_handler)

        ### INFO Вывод в файл
        #if out_file_info:
            #file_handler_info = logging.FileHandler(log_file_info, mode='w', encoding='UTF-8')
            #file_handler_info.setFormatter(log_formatter)
            #file_handler_info.setLevel(logging.INFO)
            #logger.addHandler(file_handler_info)

        ### ERROR Вывод в файл
        #if out_file_error:
            #file_handler_error = logging.FileHandler(log_file_error, mode='w', encoding='UTF-8')
            #file_handler_error.setFormatter(log_formatter)
            #file_handler_error.setLevel(logging.ERROR)
            #logger.addHandler(file_handler_error)

        #return logger
    #logger = log_init()

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(message)s"))
    logger.addHandler(sh)

    logger.info(f"s")
    with parallel_config(backend="loky", inner_max_num_threads=1):
        jobs = Parallel(n_jobs=2, verbose=1)(delayed(get_coin_data)('c', 'i', i**2, 'l') for i in range(n))
    #logger.info(f"f")
    print(jobs)
#     return jobs
