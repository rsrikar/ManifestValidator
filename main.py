import streamlit as st
import yamale
import json
import yaml
from yamale import YamaleError

def displayValidateButton(col):
   col.write('')
   col.write('')
   col.write('')
   col.write('')
   col.write('')
   col.write('')
   col.button('Validate', use_container_width=True)

st. set_page_config(layout="wide")

st.header("Snowflake listings manifest validator")

col1, col2, col3 = st.columns([3,1,3])

yamlText = col1.text_area('Enter the manifest to validate', 
'''title: "title1"
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
      - schema: "DATA_DICTIONARY_API_SCHEMA_NAME"
        domain: TABLE
        name: "TABLE_ANOTHER_NAME"
      - schema: "DATA_DICTIONARY_API_SCHEMA_NAME"
        domain: TABLE
        name: "DATA_DICTIONARY_API_TABLE_NAME"
business_needs:
  - name: "Data Quality and Cleansing"
    description: "Test listing for data cleansing"
''',
    height=600,
    placeholder="Manifest to validate ...")

try:
  
  displayValidateButton(col2)

  # read the schema
  schema = yamale.make_schema('./listingManifestSchema.yaml')
  
  # construct yaml data object to be passed to yamale validate
  yamlDataObject = yamale.make_data(content=yamlText)

  # validate the yaml data object against the schema
  yamale.validate(schema, yamlDataObject)

  # update status to say valid manifest
  col3.write('**Valid manifest**')

  # display the valid yaml as a pretty-printed JSON
  json_string = json.dumps(yaml.safe_load(yamlText))
  #col3.json(json_string)
except YamaleError as e:
    col3.write('**Validation failed!**')
    for result in e.results:
        for error in result.errors:
            col3.write('\t%s' % error)
finally:    
  col3.code(yamlText, language='yaml', line_numbers=True)
