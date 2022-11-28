from pydantic import BaseSettings


# with open(".env", "wt") as fh:
#     print("db_type=algo", file=fh)
#

class Settings(BaseSettings):
    db_url: str = "Awesome API"
    # db_port: str
    db_database: int = 50
    db_type: str = ""
    # db_user: str
    # db_password: str

    class Config:
        env_file = ".env"

settings = Settings()