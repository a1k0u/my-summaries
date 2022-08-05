class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://yandex_admin:1@localhost:5432/yandex_market"
    )
