from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.configuration.ConfigurationCONF import ConfigurationCONF
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.repository.RepositorySQLite import RepositorySQLite
from app.service.ServiceGrocery import ServiceGrocery
from app.serialize.SerializeJSON import SerializeJSON


class DependencyContainer(DeclarativeContainer):

    config = Singleton(ConfigurationCONF)
    connection = Singleton(ConnectionSQLite, config, "CONNECTION_SQLITE")
    grocery_repository = Singleton(RepositorySQLite, connection)
    service_grocery = Singleton(ServiceGrocery, config, grocery_repository)
    serializer = Singleton(SerializeJSON)

