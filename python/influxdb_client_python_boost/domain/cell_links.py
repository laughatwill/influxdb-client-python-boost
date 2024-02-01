# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class CellLinks(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        '_self': 'str',
        'view': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'view': 'view'
    }

    def __init__(self, _self=None, view=None):  # noqa: E501,D401,D403
        """CellLinks - a model defined in OpenAPI."""  # noqa: E501
        self.__self = None
        self._view = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if view is not None:
            self.view = view

    @property
    def _self(self):
        """Get the _self of this CellLinks.

        :return: The _self of this CellLinks.
        :rtype: str
        """  # noqa: E501
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Set the _self of this CellLinks.

        :param _self: The _self of this CellLinks.
        :type: str
        """  # noqa: E501
        self.__self = _self

    @property
    def view(self):
        """Get the view of this CellLinks.

        :return: The view of this CellLinks.
        :rtype: str
        """  # noqa: E501
        return self._view

    @view.setter
    def view(self, view):
        """Set the view of this CellLinks.

        :param view: The view of this CellLinks.
        :type: str
        """  # noqa: E501
        self._view = view

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, CellLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
