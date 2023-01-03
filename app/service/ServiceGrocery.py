from pathlib import Path
import os
from app.repository.RepositoryAbstract import RepositoryAbstract
from app.configuration.ConfigurationAbstract import ConfigurationAbstract

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def __create_query__(file_query):

    with open(file_query, 'r') as query:
        sql_script = query.read()
    return sql_script


class ServiceGrocery:

    def __init__(self, config: ConfigurationAbstract, repository: RepositoryAbstract):
        self.repository = repository
        self.static_folder = config.get("STATIC", "path")

    def get_all_orders(self):
        file_path = "query_grocery.sql"
        file_query = os.path.join(BASE_DIR, self.static_folder, file_path)

        query = __create_query__(file_query)

        result = self.repository.read(query).fetchall()

        return result
