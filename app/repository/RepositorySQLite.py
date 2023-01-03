from app.repository.RepositoryAbstract import RepositoryAbstract
from app.connection.ConnectionAbstract import ConnectionAbstract


class RepositorySQLite(RepositoryAbstract):

    def __init__(self, connection: ConnectionAbstract):
        self.sql = connection

    def create(self):
        pass

    # Returns result from query and the headers.
    def read(self, query: str):
        with self.sql.get_connection() as connection:
            cursor = connection.cursor()
            result = cursor.execute(query).fetchall()
            headers = list(map(lambda attr: attr[0], cursor.description))
            results = [{header: row[i] for i, header in enumerate(headers)} for row in result]

        return results

    def update(self):
        pass

    def delete(self):
        pass

