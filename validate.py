from oncollamaschemav3 import OncoLlamaModel

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