import logging

logger = logging.getLogger("MyApp")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="w", encoding="utf-8")

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a debug message")
logger.info("Program started successfully")
logger.warning("This is a warning message")
logger.error("An error has occurred")
logger.critical("Critical error! Application needs attention")
