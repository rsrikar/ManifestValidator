import streamlit as st
import yaml
from jsonschema import validate

st.write('Hello World123')

schema = """
type: object
properties:
  testing:
    type: array
    items:
      enum:
        - this
        - is
        - a
        - test
"""

good_instance = """
testing: ['this', 'is', 'a', 'test']
"""

validate(yaml.safe_load(good_instance), yaml.load(schema)) # passes

# Now let's try a bad instance...

bad_instance = """
testing: ['this', 'is', 'a', 'bad', 'test']
"""

try:
  validate(yaml.safe_load(bad_instance), yaml.load(schema))
except Exception as e:
  st.write(str(e))

# Fails with:
# ValidationError: 'bad' is not one of ['this', 'is', 'a', 'test']
#
# Failed validating 'enum' in schema['properties']['testing']['items']:
#     {'enum': ['this', 'is', 'a', 'test']}
#
# On instance['testing'][3]:
#     'bad'
