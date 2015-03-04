__author__ = 'pablo'


class Posts(object):
    def __init__(self):
        pass

    @staticmethod
    def create_post( category, content):
        categories_availables = ("gaming", 'code')
        if not isinstance(category, basestring) and not isinstance(content, basestring):
            raise ValueError

        #el nombre de la categoria debe de existir
        if category not in categories_availables:
            raise ValueError

        #Compruebbo que no inserten HTML en el post
        if "<" in content:
            raise RuntimeError
        if ">" in content:
            raise RuntimeError

        #Guardar el post en la base de datos (cuando la haya)

        #si se inserta correctamente devuelto True
        return True

    @staticmethod
    def delete_post(identifier):
        ids_availables = (1, 2, 5)

        #Debe existir el post a borrar
        if identifier not in ids_availables:
            raise ValueError

        # Borrar de la base de datos (cuando la haya)

    @staticmethod
    def get_post(identifier):
        ids_availables = (1, 2, 5)

        #Debe existir el post a obtener
        if identifier not in ids_availables:
            raise ValueError

        #traigo un post ficticio
        return "entradadeprueba"






