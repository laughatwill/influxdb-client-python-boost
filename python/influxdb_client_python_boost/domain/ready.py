# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class Ready(object):
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
        'status': 'str',
        'started': 'datetime',
        'up': 'str'
    }

    attribute_map = {
        'status': 'status',
        'started': 'started',
        'up': 'up'
    }

    def __init__(self, status=None, started=None, up=None):  # noqa: E501,D401,D403
        """Ready - a model defined in OpenAPI."""  # noqa: E501
        self._status = None
        self._started = None
        self._up = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if started is not None:
            self.started = started
        if up is not None:
            self.up = up

    @property
    def status(self):
        """Get the status of this Ready.

        :return: The status of this Ready.
        :rtype: str
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this Ready.

        :param status: The status of this Ready.
        :type: str
        """  # noqa: E501
        self._status = status

    @property
    def started(self):
        """Get the started of this Ready.

        :return: The started of this Ready.
        :rtype: datetime
        """  # noqa: E501
        return self._started

    @started.setter
    def started(self, started):
        """Set the started of this Ready.

        :param started: The started of this Ready.
        :type: datetime
        """  # noqa: E501
        self._started = started

    @property
    def up(self):
        """Get the up of this Ready.

        :return: The up of this Ready.
        :rtype: str
        """  # noqa: E501
        return self._up

    @up.setter
    def up(self, up):
        """Set the up of this Ready.

        :param up: The up of this Ready.
        :type: str
        """  # noqa: E501
        self._up = up

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
        if not isinstance(other, Ready):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
