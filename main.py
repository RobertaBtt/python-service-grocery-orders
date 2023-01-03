#!/usr/bin/env python

from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config().get('APP', 'name')


try:
    result = app.service_grocery().get_all_orders()
    result_json = app.serializer().convert(result)
    print(result_json)
except Exception as ex:
    print(ex)

