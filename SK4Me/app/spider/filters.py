import re
from SK4Me.app.app import app


@app.template_filter('normalize_name')
def normalize_name(name):
    normalized = name.replace('[', '_')
    normalized = normalized.replace(']', '_')
    normalized = normalized.replace('-', '_')
    return normalized.replace('.', '_')
