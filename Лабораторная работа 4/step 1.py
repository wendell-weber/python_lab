# TODO решите задачу
import json
def task() -> float:
    filename = "input.json"
    with open(filename, 'r') as file:
        data = json.load(file)
    sum_value = sum([item["score"] * item["weight"] for item in data])
    return round(sum_value, 3)
print(task())
