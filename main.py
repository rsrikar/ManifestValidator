import streamlit as st
import yaml
from jsonschema import validate

st.write('Hello World12')

schema = """
type: object
properties:
  title:
    type: string
  subtitle:
    type: string
  description:
    type: string
  custom_contact:
    type: string
  profile:
    type: string
  terms_of_service:
    type: object
    properties:
      type:
        enum:
          - STANDARD
          - CUSTOM
          - OFFLINE
      link:
        type: string
"""

good_instance = """
title: "title1"
subtitle: "sub title 1"
description: "listing description"
terms_of_service:
  type: "OFFLINE"
"""

bad_instance = """
testing: ['this', 'is', 'a', 'bad', 'test']
"""

try:
  validate(yaml.safe_load(good_instance), yaml.safe_load(schema)) # passes
  validate(yaml.safe_load(bad_instance), yaml.safe_load(schema))
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
