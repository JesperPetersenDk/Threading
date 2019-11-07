import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(5):
        logging.info("Main    : before creating thread %d", index)
        x = threading.Thread(target=thread_function, args=(index,))
        logging.info("Main    : before running thread")
        x.start()

    for index, thread in enumerate(thread):
        logging.info("Main    : wait for the thread to finish %d", index)
        #x.join()
        logging.info("Main    : all %d done", index)