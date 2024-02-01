# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

from influxdb_client_python_boost.domain.expression import Expression


class PipeExpression(Expression):
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
        'type': 'str',
        'argument': 'Expression',
        'call': 'CallExpression'
    }

    attribute_map = {
        'type': 'type',
        'argument': 'argument',
        'call': 'call'
    }

    def __init__(self, type=None, argument=None, call=None):  # noqa: E501,D401,D403
        """PipeExpression - a model defined in OpenAPI."""  # noqa: E501
        Expression.__init__(self)  # noqa: E501

        self._type = None
        self._argument = None
        self._call = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if argument is not None:
            self.argument = argument
        if call is not None:
            self.call = call

    @property
    def type(self):
        """Get the type of this PipeExpression.

        Type of AST node

        :return: The type of this PipeExpression.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this PipeExpression.

        Type of AST node

        :param type: The type of this PipeExpression.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def argument(self):
        """Get the argument of this PipeExpression.

        :return: The argument of this PipeExpression.
        :rtype: Expression
        """  # noqa: E501
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Set the argument of this PipeExpression.

        :param argument: The argument of this PipeExpression.
        :type: Expression
        """  # noqa: E501
        self._argument = argument

    @property
    def call(self):
        """Get the call of this PipeExpression.

        :return: The call of this PipeExpression.
        :rtype: CallExpression
        """  # noqa: E501
        return self._call

    @call.setter
    def call(self, call):
        """Set the call of this PipeExpression.

        :param call: The call of this PipeExpression.
        :type: CallExpression
        """  # noqa: E501
        self._call = call

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
        if not isinstance(other, PipeExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
