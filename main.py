import streamlit as st
import yaml

st.write('Hello World123')

from schema import Schema, SchemaError
import yaml


config_schema = Schema({
    "api": {
        "token": str
    }
})

conf_yaml = """
api:
    token: 625c2043c132485b
"""

configuration = yaml.safe_load(conf_yaml)

try:
    config_schema.validate(configuration)
    print("Configuration is valid.")
except SchemaError as se:
    st.write(str(se))
