# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

from influxdb_client_python_boost.domain.notification_endpoint_discriminator import NotificationEndpointDiscriminator


class HTTPNotificationEndpoint(NotificationEndpointDiscriminator):
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
        'url': 'str',
        'username': 'str',
        'password': 'str',
        'token': 'str',
        'method': 'str',
        'auth_method': 'str',
        'content_template': 'str',
        'headers': 'dict(str, str)',
        'id': 'str',
        'org_id': 'str',
        'user_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'description': 'str',
        'name': 'str',
        'status': 'str',
        'labels': 'list[Label]',
        'links': 'NotificationEndpointBaseLinks',
        'type': 'NotificationEndpointType'
    }

    attribute_map = {
        'url': 'url',
        'username': 'username',
        'password': 'password',
        'token': 'token',
        'method': 'method',
        'auth_method': 'authMethod',
        'content_template': 'contentTemplate',
        'headers': 'headers',
        'id': 'id',
        'org_id': 'orgID',
        'user_id': 'userID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'description': 'description',
        'name': 'name',
        'status': 'status',
        'labels': 'labels',
        'links': 'links',
        'type': 'type'
    }

    def __init__(self, url=None, username=None, password=None, token=None, method=None, auth_method=None, content_template=None, headers=None, id=None, org_id=None, user_id=None, created_at=None, updated_at=None, description=None, name=None, status='active', labels=None, links=None, type="http"):  # noqa: E501,D401,D403
        """HTTPNotificationEndpoint - a model defined in OpenAPI."""  # noqa: E501
        NotificationEndpointDiscriminator.__init__(self, id=id, org_id=org_id, user_id=user_id, created_at=created_at, updated_at=updated_at, description=description, name=name, status=status, labels=labels, links=links, type=type)  # noqa: E501

        self._url = None
        self._username = None
        self._password = None
        self._token = None
        self._method = None
        self._auth_method = None
        self._content_template = None
        self._headers = None
        self.discriminator = None

        self.url = url
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        self.method = method
        self.auth_method = auth_method
        if content_template is not None:
            self.content_template = content_template
        if headers is not None:
            self.headers = headers

    @property
    def url(self):
        """Get the url of this HTTPNotificationEndpoint.

        :return: The url of this HTTPNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._url

    @url.setter
    def url(self, url):
        """Set the url of this HTTPNotificationEndpoint.

        :param url: The url of this HTTPNotificationEndpoint.
        :type: str
        """  # noqa: E501
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        self._url = url

    @property
    def username(self):
        """Get the username of this HTTPNotificationEndpoint.

        :return: The username of this HTTPNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._username

    @username.setter
    def username(self, username):
        """Set the username of this HTTPNotificationEndpoint.

        :param username: The username of this HTTPNotificationEndpoint.
        :type: str
        """  # noqa: E501
        self._username = username

    @property
    def password(self):
        """Get the password of this HTTPNotificationEndpoint.

        :return: The password of this HTTPNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._password

    @password.setter
    def password(self, password):
        """Set the password of this HTTPNotificationEndpoint.

        :param password: The password of this HTTPNotificationEndpoint.
        :type: str
        """  # noqa: E501
        self._password = password

    @property
    def token(self):
        """Get the token of this HTTPNotificationEndpoint.

        :return: The token of this HTTPNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._token

    @token.setter
    def token(self, token):
        """Set the token of this HTTPNotificationEndpoint.

        :param token: The token of this HTTPNotificationEndpoint.
        :type: str
        """  # noqa: E501
        self._token = token

    @property
    def method(self):
        """Get the method of this HTTPNotificationEndpoint.

        :return: The method of this HTTPNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._method

    @method.setter
    def method(self, method):
        """Set the method of this HTTPNotificationEndpoint.

        :param method: The method of this HTTPNotificationEndpoint.
        :type: str
        """  # noqa: E501
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        self._method = method

    @property
    def auth_method(self):
        """Get the auth_method of this HTTPNotificationEndpoint.

        :return: The auth_method of this HTTPNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Set the auth_method of this HTTPNotificationEndpoint.

        :param auth_method: The auth_method of this HTTPNotificationEndpoint.
        :type: str
        """  # noqa: E501
        if auth_method is None:
            raise ValueError("Invalid value for `auth_method`, must not be `None`")  # noqa: E501
        self._auth_method = auth_method

    @property
    def content_template(self):
        """Get the content_template of this HTTPNotificationEndpoint.

        :return: The content_template of this HTTPNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._content_template

    @content_template.setter
    def content_template(self, content_template):
        """Set the content_template of this HTTPNotificationEndpoint.

        :param content_template: The content_template of this HTTPNotificationEndpoint.
        :type: str
        """  # noqa: E501
        self._content_template = content_template

    @property
    def headers(self):
        """Get the headers of this HTTPNotificationEndpoint.

        Customized headers.

        :return: The headers of this HTTPNotificationEndpoint.
        :rtype: dict(str, str)
        """  # noqa: E501
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Set the headers of this HTTPNotificationEndpoint.

        Customized headers.

        :param headers: The headers of this HTTPNotificationEndpoint.
        :type: dict(str, str)
        """  # noqa: E501
        self._headers = headers

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
        if not isinstance(other, HTTPNotificationEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
