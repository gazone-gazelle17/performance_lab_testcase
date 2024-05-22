import json

with open('values.json', 'r') as values_file:
    values_data = json.load(values_file)

with open('tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

values_dict = {item['id']: item['value'] for item in values_data['values']}


def fill_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'], values_dict)


fill_values(tests_data['tests'], values_dict)

with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=2)
