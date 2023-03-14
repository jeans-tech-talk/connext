def deep_get(data: dict, keys: str, default=None):
    for key in keys.split('.'):
        try:
            data = data[key]
        except KeyError:
            return default
    return data if data is not None else default
