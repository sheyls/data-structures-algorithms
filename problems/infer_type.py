from typing import Any, Dict, List, Union

def infer_type(value: Any) -> Union[str, Dict[str, Any]]:
    """Infers the type of a given value and returns a string description or a nested schema for objects."""
    if isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, bool):
        return "bool"
    elif isinstance(value, list):
        if not value:
            return "list of unknown"
        # Infer the type for each element in the list.
        element_types = {infer_type(elem) for elem in value}
        if len(element_types) == 1:
            elem_type = element_types.pop()
            return f"list of {elem_type}"
        else:
            return "list of (" + " | ".join(sorted(str(t) for t in element_types)) + ")"
    elif isinstance(value, dict):
        # Inferir el esquema para cada campo del objeto.
        schema = {}
        for k, v in value.items():
            schema[k] = infer_type(v)
        return schema
    else:
        return "unknown"

def infer_schema(dataset: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Given a list of JSON records (dictionaries), returns the schema as a dictionary mapping field names to type descriptions."""
    if not dataset:
        return {}
    
    # Asumimos que el esquema es consistente entre registros.
    schema = {}
    for record in dataset:
        for key, value in record.items():
            schema[key] = infer_type(value)
    return schema

# Ejemplo 1:
dataset1 = [{"a": 1, "b": ["hello", "world"], "c": "foo"}]
print("Schema Ejemplo 1:")
print(infer_schema(dataset1))
# Expected output:
# {'a': 'int', 'b': 'list of string', 'c': 'string'}

# Ejemplo 2 (anidado):
dataset2 = [{"a": {"b": ["hello", "world"]}, "c": "foo"}]
print("\nSchema Ejemplo 2:")
print(infer_schema(dataset2))
# Expected output:
# {'a': {'b': 'list of string'}, 'c': 'string'}
