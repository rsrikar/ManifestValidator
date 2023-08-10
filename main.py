import streamlit as st
import yaml
from jsonschema import validate

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
  usge_examples:
    type: array
    items:
      type: object
      properties:
        title:
          type: string
        description:
          type: string
        query:
          type: string
  data_dictionary:
    type: object
    properties:
      featured:
        type: object
          properties:
            database:
              type: string
            objects:
              type: array
              items:
                type: object
                  properties:
                    name:
                      type: string
                    schema:
                      type: string
                    domain:
                      enum:
                        - DATABASE
                        - SCHEMA
                        - TABLE
                        - VIEW
                        - EXTERNAL_TABLE
                        - MATERIALIZED_VIEW
                        - DIRECTORY_TABLE
                        - FUNCTION
                        - COLUMN
"""


txt = st.text_area('Manifest validator', '''
title: "title1"
subtitle: "sub title 1"
description: "listing description"
terms_of_service:
  type: "OFFLINE"
targets:
  accounts: ["Org1.Account1"]
usage_examples:
  - title: "test sql"
    description: "test sql description"
    query: "select *"
data_dictionary:
  featured: 
    database: "db_another_NAME"
      objects:
        - schema: DATA_DICTIONARY_API_SCHEMA_NAME
          domain: TABLE
          name: "TABLE_ANOTHER_NAME"
        - schema: DATA_DICTIONARY_API_SCHEMA_NAME
          domain: TABLE
          name: DATA_DICTIONARY_API_TABLE_NAME
''',
height=500,
placeholder="Manifest to validate ...")

try:
  validate(yaml.safe_load(txt), yaml.safe_load(schema)) # passes
  st.write("Valid manifest")
except Exception as e:
  st.write("Inalid manifest")
  st.write(str(e))
