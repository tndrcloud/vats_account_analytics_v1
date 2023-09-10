import subprocess

from core.exceptions import AlembicException


def init_db():
    response = subprocess.run(["alembic", "upgrade", "head"])
    if response.returncode != 0:
        raise AlembicException("Migration failure")
    