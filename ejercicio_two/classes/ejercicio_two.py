__author__ = 'pablo'


class EjercicioTwo(object):
    def __init__(self):
        pass

    @staticmethod
    def sum(*strs):
        result = None
        if len(strs) < 2 or len(strs) > 10:
            raise SyntaxError
        if isinstance(strs[0], int):
            result = 0
        elif isinstance(strs[0], float):
            result = 0.0
        else:
            result = ""
        for arg_tr in strs:
            if isinstance(result, basestring):
                if not isinstance(arg_tr, basestring):
                    arg_tr = str(arg_tr)
            elif isinstance(arg_tr, basestring):
                result = str(result)

            result += arg_tr

        return result