import json
import os
import re

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

with open(os.path.join(project_dir, 'src', 'config.json')) as f:
    project_metadata = json.load(f)

project_levels = re.split(r",\s*", project_metadata['levels'])

