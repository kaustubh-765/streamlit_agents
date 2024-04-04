import json

class OutputTransformer:
    def __init__(self, json_data):
        self.json_data = json.loads(json_data)
        self.transformed_data = {"data": [], "meta": {}}
    
    def transform(self):
        for key, value in self.json_data.items():
            if key.lower() == "multiple_choice":
                # Move the multiple choice to data
                self.transformed_data["data"].append({"type": key.lower(), "value": value})
            elif isinstance(value, (str, int, float)):
                self.transformed_data["data"].append({"type": key.lower(), "value": value})
            elif isinstance(value, list) and all(isinstance(item, dict) for item in value):
                transformed_list = [{k: v for k, v in item.items()} for item in value]
                self.transformed_data["data"].append({"type": key.lower(), "value": transformed_list})
            else:
                self.transformed_data["meta"][key.lower()] = value
        
        return json.dumps(self.transformed_data, indent=4)