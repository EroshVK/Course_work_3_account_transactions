from utils import *

data = load_operations()
executed_operations = select_by_state(data)
last_operations = last_executed_operations(executed_operations)
for item in output(last_operations):
    print(item)
