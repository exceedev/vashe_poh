from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from logging.config import fileConfig

import os
import sys

from db import engine, Base
from models import *
from config import Config

current_path = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(current_path, '..')
sys.path.append(ROOT_PATH)


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = Config.DB_CONN

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()