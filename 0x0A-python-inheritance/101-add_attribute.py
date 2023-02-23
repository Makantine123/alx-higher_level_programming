#!/usr/bin/python3
""" Program that adds a new attribute to an object if its possible """


def add_attribute(obj, att, value):
    """ functions attempts to add a new attribut to object 
        Args:
            obj: Object Name
            att: Attribute Name
            value: value of attribute
        Raises:
            TypeError: cant't add new attribut
        Returns:
            None
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TyeError("can't add new attribute")
