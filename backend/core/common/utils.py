def deep_get(dictionary, keys, default=None):
    """
    Example:
        validated_data = {'bank_account': {'account_type': 'Savings Account'}}
        deep_get(validated_data, 'bank_account.account_type') # => Savings Account
        deep_get(validated_data, 'bank_account.branch') # => None
        deep_get(validated_data, 'address') # => None
    """
    keys_list = keys.split('.')
    for key in keys_list:
        try:
            dictionary = dictionary[key]
        except (TypeError, KeyError):
            return default
    return dictionary if dictionary is not None else default
