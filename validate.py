import json
from oncollamaschemav3.oncollamaschemav3 import OncoLlamaModel
from pydantic import ValidationError

"""
validate.py - simple functions to validate schema and json 

Run in CLI to validate directly schema
"""

def validate_json(json_str):
    try:
        parsed = json.loads(json_str)
        OncoLlamaModel(**parsed)
        return True, "Valid", parsed
    except json.JSONDecodeError as e:
        return False, f"JSON Parse Error: {e}", None
    except ValidationError as e:
        return False, f"Schema Validation Error: {e}", None
    except Exception as e:
        return False, f"Validation Error: {e}", None

def validate_schema():
    try:
        schema = OncoLlamaModel.model_json_schema()
        print("Schema validation successful")
        print(f"Properties: {len(schema.get('properties', {}))}")
        print(f"Definitions: {len(schema.get('$defs', {}))}")
    except Exception as e:
        print(f"Schema validation failed: {e}")
        exit(1)

if __name__ == "__main__":
    validate_schema()