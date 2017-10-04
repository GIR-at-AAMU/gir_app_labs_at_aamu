
_registry = {}

def routes():
    return _registry.items()

def add_page(url_path, handler):
    _registry[url_path] = handler
