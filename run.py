from test import simple_test
import json

grade['grade'] = simple_test(5)
with open('./grade.json', 'w') as f:
  json.dump(grade, f)
