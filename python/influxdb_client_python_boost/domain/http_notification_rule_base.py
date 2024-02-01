# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

from influxdb_client_python_boost.domain.notification_rule_discriminator import NotificationRuleDiscriminator


class HTTPNotificationRuleBase(NotificationRuleDiscriminator):
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
        'url': 'str',
        'latest_completed': 'datetime',
        'last_run_status': 'str',
        'last_run_error': 'str',
        'id': 'str',
        'endpoint_id': 'str',
        'org_id': 'str',
        'task_id': 'str',
        'owner_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'status': 'TaskStatusType',
        'name': 'str',
        'sleep_until': 'str',
        'every': 'str',
        'offset': 'str',
        'runbook_link': 'str',
        'limit_every': 'int',
        'limit': 'int',
        'tag_rules': 'list[TagRule]',
        'description': 'str',
        'status_rules': 'list[StatusRule]',
        'labels': 'list[Label]',
        'links': 'NotificationRuleBaseLinks'
    }

    attribute_map = {
        'type': 'type',
        'url': 'url',
        'latest_completed': 'latestCompleted',
        'last_run_status': 'lastRunStatus',
        'last_run_error': 'lastRunError',
        'id': 'id',
        'endpoint_id': 'endpointID',
        'org_id': 'orgID',
        'task_id': 'taskID',
        'owner_id': 'ownerID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'status': 'status',
        'name': 'name',
        'sleep_until': 'sleepUntil',
        'every': 'every',
        'offset': 'offset',
        'runbook_link': 'runbookLink',
        'limit_every': 'limitEvery',
        'limit': 'limit',
        'tag_rules': 'tagRules',
        'description': 'description',
        'status_rules': 'statusRules',
        'labels': 'labels',
        'links': 'links'
    }

    def __init__(self, type=None, url=None, latest_completed=None, last_run_status=None, last_run_error=None, id=None, endpoint_id=None, org_id=None, task_id=None, owner_id=None, created_at=None, updated_at=None, status=None, name=None, sleep_until=None, every=None, offset=None, runbook_link=None, limit_every=None, limit=None, tag_rules=None, description=None, status_rules=None, labels=None, links=None):  # noqa: E501,D401,D403
        """HTTPNotificationRuleBase - a model defined in OpenAPI."""  # noqa: E501
        NotificationRuleDiscriminator.__init__(self, latest_completed=latest_completed, last_run_status=last_run_status, last_run_error=last_run_error, id=id, endpoint_id=endpoint_id, org_id=org_id, task_id=task_id, owner_id=owner_id, created_at=created_at, updated_at=updated_at, status=status, name=name, sleep_until=sleep_until, every=every, offset=offset, runbook_link=runbook_link, limit_every=limit_every, limit=limit, tag_rules=tag_rules, description=description, status_rules=status_rules, labels=labels, links=links)  # noqa: E501

        self._type = None
        self._url = None
        self.discriminator = None

        self.type = type
        if url is not None:
            self.url = url

    @property
    def type(self):
        """Get the type of this HTTPNotificationRuleBase.

        :return: The type of this HTTPNotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this HTTPNotificationRuleBase.

        :param type: The type of this HTTPNotificationRuleBase.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def url(self):
        """Get the url of this HTTPNotificationRuleBase.

        :return: The url of this HTTPNotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._url

    @url.setter
    def url(self, url):
        """Set the url of this HTTPNotificationRuleBase.

        :param url: The url of this HTTPNotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._url = url

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
        if not isinstance(other, HTTPNotificationRuleBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
