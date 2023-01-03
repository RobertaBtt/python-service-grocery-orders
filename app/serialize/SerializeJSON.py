import json


class SerializeJSON():

    @staticmethod
    def convert(input_data: list):

        for element in input_data:
            element['item_categories'] = SerializeJSON.from_str_to_list(element['item_categories'])
            element['labels'] = SerializeJSON.from_str_to_list(element.pop('extra_categories'))

            element['case'] = {
                'quantity': element.pop('case_quantity'),
                'unit': element.pop('case_unit')
            }
            element['order'] = {
                'quantity': element.pop('order_quantity'),
                'unit': element.pop('order_unit')
            }
            element['inventory'] = {
                'quantity': element.pop('inventory_quantity'),
                'unit': 'CS'
            }

        return json.dumps(input_data)

    @staticmethod
    def from_str_to_list(input_str):
        return input_str.strip('][').replace("'", "").split(', ')
