from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    database_username: str 
    database_hostname: str 
    database_port: int
    database_password: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    debug: bool = True


    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f'mysql+pymysql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}'


settings = Settings()
