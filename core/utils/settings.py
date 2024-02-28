from dataclasses import dataclass

from environs import Env


@dataclass
class Database:
    host: str
    port: int
    username: str
    password: str
    database_name: str


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    channel_id: int


@dataclass
class Redis:
    url: str


@dataclass
class Settings:
    bots: Bots
    database: Database
    redis: Redis


def get_settings(path: str) -> Settings:
    env = Env()
    env.read_env(path)

    try:
        bot_token = env.str('TOKEN')
        admin_id = env.int('ADMIN_ID')
        channel_id = env.int('CHANNEL_ID')

        db_host = env.str('DB_HOST')
        db_port = env.int('DB_PORT')
        db_username = env.str('DB_USERNAME')
        db_password = env.str('DB_PASSWORD')
        db_name = env.str('DB_NAME')

        redis_url = env.str('REDIS_URL')
    except Exception as e:
        raise ValueError("Ошибка при чтении переменных окружения: " + str(e))

    return Settings(
        bots=Bots(
            bot_token=bot_token,
            admin_id=admin_id,
            channel_id=channel_id,
        ),
        database=Database(
            host=db_host,
            port=db_port,
            username=db_username,
            password=db_password,
            database_name=db_name
        ),
        redis=Redis(url=redis_url)
    )


settings = get_settings('.env')
