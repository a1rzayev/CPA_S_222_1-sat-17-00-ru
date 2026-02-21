import logging # модуль(библиотека) для работы с отчетами(логгингом) 

# определяем базовую конфигурацию(настройку) для логирования
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

# деление и проверка 
def divide(a, b):
    logging.info(f"выполняется деление: {a} / {b}")
    try:
        result = a / b
    except ZeroDivisionError: # что делать при ошибке(отладчики)
        logging.error("на 0 делить нельзя!")
    except ValueError:
        logging.error("неверные числа!")
    except Exception as e:
        logging.error("неизвестная ошибка!", e)

logging.info("начало программы")

divide(10, 2)
divide(5, 0)

logging.warning("это предупреждение!")
logging.info("конец программы!")