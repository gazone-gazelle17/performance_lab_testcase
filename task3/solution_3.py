import sys
import json


def load_json(file_path):
    with open(file_path, 'r') as values_file:
        return json.load(values_file)


def save_json(data, file_path):
    with open(file_path, 'w') as tests_file:
        json.dump(data, tests_file, indent=2)


def fill_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'], values_dict)


def main():
    if len(sys.argv) != 4:
        print("""
              Введите команду:
              python3 solution_3.py <values.json> <tests.json> <report.json>
              """
              )
        return

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)
    values_dict = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_dict)
    save_json(tests_data, report_file)


if __name__ == "__main__":
    main()
