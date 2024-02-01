# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class NotificationRuleBase(object):
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

    def __init__(self, latest_completed=None, last_run_status=None, last_run_error=None, id=None, endpoint_id=None, org_id=None, task_id=None, owner_id=None, created_at=None, updated_at=None, status=None, name=None, sleep_until=None, every=None, offset=None, runbook_link=None, limit_every=None, limit=None, tag_rules=None, description=None, status_rules=None, labels=None, links=None):  # noqa: E501,D401,D403
        """NotificationRuleBase - a model defined in OpenAPI."""  # noqa: E501
        self._latest_completed = None
        self._last_run_status = None
        self._last_run_error = None
        self._id = None
        self._endpoint_id = None
        self._org_id = None
        self._task_id = None
        self._owner_id = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._name = None
        self._sleep_until = None
        self._every = None
        self._offset = None
        self._runbook_link = None
        self._limit_every = None
        self._limit = None
        self._tag_rules = None
        self._description = None
        self._status_rules = None
        self._labels = None
        self._links = None
        self.discriminator = None

        if latest_completed is not None:
            self.latest_completed = latest_completed
        if last_run_status is not None:
            self.last_run_status = last_run_status
        if last_run_error is not None:
            self.last_run_error = last_run_error
        if id is not None:
            self.id = id
        self.endpoint_id = endpoint_id
        self.org_id = org_id
        if task_id is not None:
            self.task_id = task_id
        if owner_id is not None:
            self.owner_id = owner_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.status = status
        self.name = name
        if sleep_until is not None:
            self.sleep_until = sleep_until
        if every is not None:
            self.every = every
        if offset is not None:
            self.offset = offset
        if runbook_link is not None:
            self.runbook_link = runbook_link
        if limit_every is not None:
            self.limit_every = limit_every
        if limit is not None:
            self.limit = limit
        if tag_rules is not None:
            self.tag_rules = tag_rules
        if description is not None:
            self.description = description
        self.status_rules = status_rules
        if labels is not None:
            self.labels = labels
        if links is not None:
            self.links = links

    @property
    def latest_completed(self):
        """Get the latest_completed of this NotificationRuleBase.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)) of the latest scheduled and completed run.

        :return: The latest_completed of this NotificationRuleBase.
        :rtype: datetime
        """  # noqa: E501
        return self._latest_completed

    @latest_completed.setter
    def latest_completed(self, latest_completed):
        """Set the latest_completed of this NotificationRuleBase.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)) of the latest scheduled and completed run.

        :param latest_completed: The latest_completed of this NotificationRuleBase.
        :type: datetime
        """  # noqa: E501
        self._latest_completed = latest_completed

    @property
    def last_run_status(self):
        """Get the last_run_status of this NotificationRuleBase.

        :return: The last_run_status of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._last_run_status

    @last_run_status.setter
    def last_run_status(self, last_run_status):
        """Set the last_run_status of this NotificationRuleBase.

        :param last_run_status: The last_run_status of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._last_run_status = last_run_status

    @property
    def last_run_error(self):
        """Get the last_run_error of this NotificationRuleBase.

        :return: The last_run_error of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._last_run_error

    @last_run_error.setter
    def last_run_error(self, last_run_error):
        """Set the last_run_error of this NotificationRuleBase.

        :param last_run_error: The last_run_error of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._last_run_error = last_run_error

    @property
    def id(self):
        """Get the id of this NotificationRuleBase.

        :return: The id of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this NotificationRuleBase.

        :param id: The id of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def endpoint_id(self):
        """Get the endpoint_id of this NotificationRuleBase.

        :return: The endpoint_id of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Set the endpoint_id of this NotificationRuleBase.

        :param endpoint_id: The endpoint_id of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        if endpoint_id is None:
            raise ValueError("Invalid value for `endpoint_id`, must not be `None`")  # noqa: E501
        self._endpoint_id = endpoint_id

    @property
    def org_id(self):
        """Get the org_id of this NotificationRuleBase.

        The ID of the organization that owns this notification rule.

        :return: The org_id of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this NotificationRuleBase.

        The ID of the organization that owns this notification rule.

        :param org_id: The org_id of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
        self._org_id = org_id

    @property
    def task_id(self):
        """Get the task_id of this NotificationRuleBase.

        The ID of the task associated with this notification rule.

        :return: The task_id of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Set the task_id of this NotificationRuleBase.

        The ID of the task associated with this notification rule.

        :param task_id: The task_id of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._task_id = task_id

    @property
    def owner_id(self):
        """Get the owner_id of this NotificationRuleBase.

        The ID of creator used to create this notification rule.

        :return: The owner_id of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Set the owner_id of this NotificationRuleBase.

        The ID of creator used to create this notification rule.

        :param owner_id: The owner_id of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._owner_id = owner_id

    @property
    def created_at(self):
        """Get the created_at of this NotificationRuleBase.

        :return: The created_at of this NotificationRuleBase.
        :rtype: datetime
        """  # noqa: E501
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Set the created_at of this NotificationRuleBase.

        :param created_at: The created_at of this NotificationRuleBase.
        :type: datetime
        """  # noqa: E501
        self._created_at = created_at

    @property
    def updated_at(self):
        """Get the updated_at of this NotificationRuleBase.

        :return: The updated_at of this NotificationRuleBase.
        :rtype: datetime
        """  # noqa: E501
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Set the updated_at of this NotificationRuleBase.

        :param updated_at: The updated_at of this NotificationRuleBase.
        :type: datetime
        """  # noqa: E501
        self._updated_at = updated_at

    @property
    def status(self):
        """Get the status of this NotificationRuleBase.

        :return: The status of this NotificationRuleBase.
        :rtype: TaskStatusType
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this NotificationRuleBase.

        :param status: The status of this NotificationRuleBase.
        :type: TaskStatusType
        """  # noqa: E501
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        self._status = status

    @property
    def name(self):
        """Get the name of this NotificationRuleBase.

        Human-readable name describing the notification rule.

        :return: The name of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this NotificationRuleBase.

        Human-readable name describing the notification rule.

        :param name: The name of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def sleep_until(self):
        """Get the sleep_until of this NotificationRuleBase.

        :return: The sleep_until of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._sleep_until

    @sleep_until.setter
    def sleep_until(self, sleep_until):
        """Set the sleep_until of this NotificationRuleBase.

        :param sleep_until: The sleep_until of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._sleep_until = sleep_until

    @property
    def every(self):
        """Get the every of this NotificationRuleBase.

        The notification repetition interval.

        :return: The every of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._every

    @every.setter
    def every(self, every):
        """Set the every of this NotificationRuleBase.

        The notification repetition interval.

        :param every: The every of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._every = every

    @property
    def offset(self):
        """Get the offset of this NotificationRuleBase.

        Duration to delay after the schedule, before executing check.

        :return: The offset of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Set the offset of this NotificationRuleBase.

        Duration to delay after the schedule, before executing check.

        :param offset: The offset of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._offset = offset

    @property
    def runbook_link(self):
        """Get the runbook_link of this NotificationRuleBase.

        :return: The runbook_link of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._runbook_link

    @runbook_link.setter
    def runbook_link(self, runbook_link):
        """Set the runbook_link of this NotificationRuleBase.

        :param runbook_link: The runbook_link of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._runbook_link = runbook_link

    @property
    def limit_every(self):
        """Get the limit_every of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limit cannot be empty.

        :return: The limit_every of this NotificationRuleBase.
        :rtype: int
        """  # noqa: E501
        return self._limit_every

    @limit_every.setter
    def limit_every(self, limit_every):
        """Set the limit_every of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limit cannot be empty.

        :param limit_every: The limit_every of this NotificationRuleBase.
        :type: int
        """  # noqa: E501
        self._limit_every = limit_every

    @property
    def limit(self):
        """Get the limit of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limitEvery cannot be empty.

        :return: The limit of this NotificationRuleBase.
        :rtype: int
        """  # noqa: E501
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Set the limit of this NotificationRuleBase.

        Don't notify me more than <limit> times every <limitEvery> seconds. If set, limitEvery cannot be empty.

        :param limit: The limit of this NotificationRuleBase.
        :type: int
        """  # noqa: E501
        self._limit = limit

    @property
    def tag_rules(self):
        """Get the tag_rules of this NotificationRuleBase.

        List of tag rules the notification rule attempts to match.

        :return: The tag_rules of this NotificationRuleBase.
        :rtype: list[TagRule]
        """  # noqa: E501
        return self._tag_rules

    @tag_rules.setter
    def tag_rules(self, tag_rules):
        """Set the tag_rules of this NotificationRuleBase.

        List of tag rules the notification rule attempts to match.

        :param tag_rules: The tag_rules of this NotificationRuleBase.
        :type: list[TagRule]
        """  # noqa: E501
        self._tag_rules = tag_rules

    @property
    def description(self):
        """Get the description of this NotificationRuleBase.

        An optional description of the notification rule.

        :return: The description of this NotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this NotificationRuleBase.

        An optional description of the notification rule.

        :param description: The description of this NotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def status_rules(self):
        """Get the status_rules of this NotificationRuleBase.

        List of status rules the notification rule attempts to match.

        :return: The status_rules of this NotificationRuleBase.
        :rtype: list[StatusRule]
        """  # noqa: E501
        return self._status_rules

    @status_rules.setter
    def status_rules(self, status_rules):
        """Set the status_rules of this NotificationRuleBase.

        List of status rules the notification rule attempts to match.

        :param status_rules: The status_rules of this NotificationRuleBase.
        :type: list[StatusRule]
        """  # noqa: E501
        if status_rules is None:
            raise ValueError("Invalid value for `status_rules`, must not be `None`")  # noqa: E501
        self._status_rules = status_rules

    @property
    def labels(self):
        """Get the labels of this NotificationRuleBase.

        :return: The labels of this NotificationRuleBase.
        :rtype: list[Label]
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this NotificationRuleBase.

        :param labels: The labels of this NotificationRuleBase.
        :type: list[Label]
        """  # noqa: E501
        self._labels = labels

    @property
    def links(self):
        """Get the links of this NotificationRuleBase.

        :return: The links of this NotificationRuleBase.
        :rtype: NotificationRuleBaseLinks
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this NotificationRuleBase.

        :param links: The links of this NotificationRuleBase.
        :type: NotificationRuleBaseLinks
        """  # noqa: E501
        self._links = links

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
        if not isinstance(other, NotificationRuleBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
