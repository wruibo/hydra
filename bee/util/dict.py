"""
    case insensitive dict
"""


class CaseInsensitiveDict(dict):
    def __init__(self, seq={}, **kwargs):
        super(CaseInsensitiveDict, self).__init__(seq, **kwargs)

    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(self._lower_key(key), (key, value))

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(self._lower_key(key))[1]

    def __delitem__(self, key):
        del self[self._lower_key(key)]

    def __iter__(self):
        return self.keys()

    def __eq__(self, other):
        if not isinstance(other, CaseInsensitiveDict):
            other = CaseInsensitiveDict(other)
        return dict(self.lower_items()) == dict(other.lower_items())

    def keys(self):
        return (key for key, value in super(CaseInsensitiveDict, self).values())

    def values(self):
        return (value for key, value in super(CaseInsensitiveDict, self).values())

    def items(self):
        return ((key, value) for key, value in super(CaseInsensitiveDict, self).values())

    def lower_items(self):
        return ((self._lower_key(key), value) for key, value in super(CaseInsensitiveDict, self).values())

    def _lower_key(self, key):
        if isinstance(key, str):
            return key.lower()
        return key


if __name__ == "__main__":
    a = CaseInsensitiveDict()
    a["ABC"] = "Abc"
    a["aBD"] = "Abc"
    a["eFg"] = "eFG"

    b = CaseInsensitiveDict()
    b["abc"] = "Abc"
    b["aBD"] = "Abc"
    b["eFg"] = "eFG"

    c = {"a":"A"}
    d = {"a":"a"}
    if c==d:
        print("c==d")

    if a == b:
        print("a==b")
    else:
        print("a != b")

    print(a)
    print(a.keys())
    for key in a.keys():
        print(key)
    print(a.values())
    for val in a.values():
        print(val)
    print(a.items())
