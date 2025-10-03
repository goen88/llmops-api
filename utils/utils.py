import json


def output_json(data,indent=4):
    """
       打印参数。如果参数是有结构的（如字典或列表），则以格式化的 JSON 形式打印；
       否则，直接打印该值。
       """
    if hasattr(data, 'model_dump_json'):
        data = json.loads(data.model_dump_json())

    if (isinstance(data, (list, dict))):
        print(json.dumps(
            data,
            indent=indent,
            ensure_ascii=False
        ))
    else:
        print(data)
