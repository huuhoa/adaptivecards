import json


class PropertyType:
    def __init__(self, type, key_name=None):
        self.key_name = key_name
        self.type = type

    def __get__(self, instance, owner):
        return instance.get_data(self.key_name)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f'{self.key_name} must be of type(s) {self.type} (got {value!r})')
        instance.set_data(self.key_name, value)

    def __set_name__(self, owner, name):
        if self.key_name is None:
            self.key_name = name


class AdaptiveCardJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BareObject):
            return obj._data

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)



class BareObject():
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._data = {}

        # init data
        if kwargs:
            for prop in tuple(kwargs):
                try:
                    self.__setattr__(prop, kwargs[prop])
                except AttributeError:
                    pass

    def __str__(self):
        return json.dumps(self.render(), sort_keys=True, indent=2, cls=AdaptiveCardJSONEncoder)

    def __repr__(self):
        return self.__str__()

    def render(self):
        """
        Transform instance object to dict that follows the schema of adaptivecards.io
        Returns
        -------
        dict : data follow schema of adaptivecards
        """
        return self._data

    def get_data(self, key):
        return self._data.get(key)

    def set_data(self, key, value):
        self._data[key] = value


class Element(BareObject):
    element_type = 'None'
    fallback = PropertyType(type=str)
    height = PropertyType(type=str)
    separator = PropertyType(type=bool)
    spacing = PropertyType(type=str)
    visible = PropertyType(key_name='isVisible', type=bool)
    id = PropertyType(type=str)
    requires = PropertyType(type=dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data['type'] = self.element_type
