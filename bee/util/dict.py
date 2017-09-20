"""
    case insensitive dict
"""
import collections


class CaseInsensitiveDict(collections.MutableMapping):
    def __init__(self, data=None, **kwargs):
        self._store = collections.OrderedDict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        # Use the lowercased key for lookups, but store the actual
        # key alongside the value.
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key):
        return self._store[key.lower()][1]

    def __delitem__(self, key):
        del self._store[key.lower()]

    def __iter__(self):
        return (casedkey for casedkey, mappedvalue in self._store.values())

    def __len__(self):
        return len(self._store)

    def __eq__(self, other):
        if isinstance(other, collections.Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    def __repr__(self):
        return str(dict(self.items()))

    def copy(self):
        return CaseInsensitiveDict(self._store.values())

    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        return (
            (lowerkey, keyval[1])
            for (lowerkey, keyval)
            in self._store.items()
        )


if __name__ == "__main__":
    x = {"a":2, "b":3}
    e = CaseInsensitiveDict(**x)
    print(e)

    a = CaseInsensitiveDict()
    a["ABC"] = "Abcd"
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

    for v in b.items():
        print(v)
