def parse(QUERY_STRING: str) -> list:
    return QUERY_STRING.lstrip('/?').split('&')
