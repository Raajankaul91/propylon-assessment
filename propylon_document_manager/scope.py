class ScopeException(Exception):
    pass

class Scopes():

    """
        Checks the scope of a user for a file
    """
    @staticmethod
    def in_user_scope(user_id, *, file_user_id=None):

        if user_id is None:
            raise Exception("No user identification was supplied.")

        if file_user_id is None :
            raise Exception("file owner not specified")

        if user_id != file_user_id:
            raise ScopeException("The user is not allowed access to the file.")



