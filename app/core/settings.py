from pydantic import BaseSettings
from fastapi.security import OAuth2PasswordBearer


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    s3_url: str
    s3_access_key_id: str
    s3_secret_access_key: str
    s3_default_region: str
    s3_bucket: str
    s3_version: str
    s3_endpoint: str

    class Config:
        env_file = ".env"


settings = Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login') 