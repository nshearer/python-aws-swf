

def dpath(data, *path, default=None, required=False):

    if data is None:
        raise ValueError("Passed in None for data")

    path_so_far = list()
    for hop in path:
        try:
            data = data[hop]
            path_so_far.append(hop)
        except KeyError:
            return default
        except ValueError:
            raise Exception("data[%s] is a %s, not dict" % (
                ']['.join(path_so_far), data.__class__.__name__
            ))

        if data is None:
            break

    if data is None:
        if required:
            raise KeyError("No value at data[%s]" % (']['.join(path)))
        else:
            return default
    return data

