import os
from pydantic import BaseModel, ValidationError, validator


class Settings(BaseModel):
    port: int
    workers: int
    files_dir: str
    base_url: str
    token: str
    github_org: str
    firmware_github_token: str
    firmware_github_repo: str
    firmware_minimum_files: int
    qFlipper_github_token: str
    qFlipper_github_repo: str
    qFlipper_minimum_files: int
    public_paths: list[str]

    @validator("*", each_item=True)
    def emptyString(cls, elem):
        if isinstance(elem, str):
            if not elem or elem.isspace():
                raise ValueError("Variable is empty")
        return elem


settings = Settings(
    port=8000,
    workers=1,
    files_dir=os.getenv("INDEXER_FILES_DIR"),
    base_url=os.getenv("INDEXER_BASE_URL"),
    token=os.getenv("INDEXER_TOKEN"),
    github_org=os.getenv("INDEXER_GITHUB_ORGANIZATION"),
    firmware_github_token=os.getenv("INDEXER_FIRMWARE_GITHUB_TOKEN"),
    firmware_github_repo=os.getenv("INDEXER_FIRMWARE_GITHUB_REPO"),
    firmware_minimum_files=14,
    qFlipper_github_token=os.getenv("INDEXER_QFLIPPER_GITHUB_TOKEN"),
    qFlipper_github_repo=os.getenv("INDEXER_QFLIPPER_GITHUB_REPO"),
    qFlipper_minimum_files=4,
    public_paths=["/firmware/directory.json", "/qFlipper/directory.json"],
)
