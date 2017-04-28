class Location(object):

    def __init__(self, **kwargs):
        if kwargs.get('lat') is None or kwargs.get('lng') is None:
            raise ValueError('Missing lat or lng.')

        self.lat = float(kwargs.get('lat'))
        self.lng = float(kwargs.get('lng'))
        self.name = kwargs.get('name')
        self.category = kwargs.get('category')
        self.weight = kwargs.get('weight')

    def to_dict(self):
        return {
            'lat': self.lat,
            'lng': self.lng,
            'name': self.name,
            'category': self.category,
            'weight': self.weight,
        }
