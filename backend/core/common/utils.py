def deep_get(data: dict, key: str, default=None):
    for key in key.split('.'):
        try:
            data = data[key]
        except KeyError:
            return default
    return data if data is not None else default
