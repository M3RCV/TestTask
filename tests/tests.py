#вместо тестов тут находится файл отключения всех uvicorn процессов
import os, signal
os.kill(os.getpid(), signal.SIGINT)