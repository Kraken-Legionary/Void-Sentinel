# logging_config.py
import logging

def setup_logging():
    # Настройка базового конфигуратора для логирования
    logging.basicConfig(
        filename='bot.log',  # Имя файла для логов
        filemode='a',         # Режим записи: 'a' для добавления к существующим логам, 'w' для перезаписи
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO   # Уровень логирования
    )

# Пример использования:
if __name__ == "__main__":
    setup_logging()
    logging.info('Logging setup complete.')
