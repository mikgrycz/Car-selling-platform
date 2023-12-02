from dotenv import load_dotenv
from alembic.config import Config
from alembic import command

load_dotenv()
# create a Config object
config = Config("alembic.ini")
# run the Alembic revision command
command.revision(config, autogenerate=True)
# run the Alembic upgrade command
command.upgrade(config, "head")