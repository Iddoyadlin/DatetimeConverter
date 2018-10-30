from functools import reduce


class Converter:
    FORMAT_MAP = {
        '%d': 'dd',
        '%Y': 'yyyy',
        '%y': 'yy',
        '%B': 'MMMM',
        '%b': 'MMM',
        '%m': 'MM',
        '%H': 'HH',
        '%M': 'mm',
        '%S': 'ss',
        '%f': '',
    }

    def convert_to_iso_8601(self, format):
        return reduce(lambda a, kv: a.replace(*kv), self.FORMAT_MAP.items(), format)
