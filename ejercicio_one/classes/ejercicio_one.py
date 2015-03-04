__author__ = 'pablo'


class EjercicioOne(object):
    def __init__(self):
        pass

    @staticmethod
    def concat(*strs):
        result = ""
        if len(strs) < 2 or len(strs) > 10:
            raise SyntaxError
        for arg_tr in strs:
            if not isinstance(arg_tr, basestring):
                raise ValueError
            if len(arg_tr) > 10:
                raise ValueError

            result += arg_tr.strip()
        return result



