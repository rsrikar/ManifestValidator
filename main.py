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
  auto_fulfillment:
    type: object
    properties:
      refresh_schedule:
        type: string
      refresh_type:
        enum:
          - FULL_DATABASE
          - SUB_DATABASE
  targets:
    type: object
    properties:
      accounts:
        type: array
        items:
          type: string
"""


txt = st.text_area('Manifest validator', '''
title: "title1"
subtitle: "sub title 1"
description: "listing description"
terms_of_service:
  type: "OFFLINE"
targets:
  accounts: ["Org1.Account1"]
''')

try:
  validate(yaml.safe_load(txt), yaml.safe_load(schema)) # passes
  st.write("Valid manifest")
except Exception as e:
  st.write(str(e))
