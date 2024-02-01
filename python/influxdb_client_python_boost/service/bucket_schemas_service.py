# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from influxdb_client_python_boost.service._base_service import _BaseService


class BucketSchemasService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """BucketSchemasService - a operation defined in OpenAPI."""
        super().__init__(api_client)

    def create_measurement_schema(self, bucket_id, measurement_schema_create_request, **kwargs):  # noqa: E501,D401,D403
        """Create a measurement schema for a bucket.

        Creates an _explict_ measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema) for a bucket.  _Explicit_ schemas are used to enforce column names, tags, fields, and data types for your data.  By default, buckets have an _implicit_ schema-type (`"schemaType": "implicit"`) that conforms to your data.  Use this endpoint to create schemas that prevent non-conforming write requests.  #### Limitations  - Buckets must be created with the "explict" `schemaType` in order to use schemas.  #### Related guides  - [Manage bucket schemas](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/). - [Create a bucket with an explicit schema](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/create-bucket/#create-a-bucket-with-an-explicit-schema)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_measurement_schema(bucket_id, measurement_schema_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Adds a schema for the specified bucket. (required)
        :param MeasurementSchemaCreateRequest measurement_schema_create_request: (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_measurement_schema_with_http_info(bucket_id, measurement_schema_create_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_measurement_schema_with_http_info(bucket_id, measurement_schema_create_request, **kwargs)  # noqa: E501
            return data

    def create_measurement_schema_with_http_info(self, bucket_id, measurement_schema_create_request, **kwargs):  # noqa: E501,D401,D403
        """Create a measurement schema for a bucket.

        Creates an _explict_ measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema) for a bucket.  _Explicit_ schemas are used to enforce column names, tags, fields, and data types for your data.  By default, buckets have an _implicit_ schema-type (`"schemaType": "implicit"`) that conforms to your data.  Use this endpoint to create schemas that prevent non-conforming write requests.  #### Limitations  - Buckets must be created with the "explict" `schemaType` in order to use schemas.  #### Related guides  - [Manage bucket schemas](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/). - [Create a bucket with an explicit schema](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/create-bucket/#create-a-bucket-with-an-explicit-schema)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_measurement_schema_with_http_info(bucket_id, measurement_schema_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Adds a schema for the specified bucket. (required)
        :param MeasurementSchemaCreateRequest measurement_schema_create_request: (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not self._is_cloud_instance():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._create_measurement_schema_prepare(bucket_id, measurement_schema_create_request, **kwargs)  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchema',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def create_measurement_schema_async(self, bucket_id, measurement_schema_create_request, **kwargs):  # noqa: E501,D401,D403
        """Create a measurement schema for a bucket.

        Creates an _explict_ measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema) for a bucket.  _Explicit_ schemas are used to enforce column names, tags, fields, and data types for your data.  By default, buckets have an _implicit_ schema-type (`"schemaType": "implicit"`) that conforms to your data.  Use this endpoint to create schemas that prevent non-conforming write requests.  #### Limitations  - Buckets must be created with the "explict" `schemaType` in order to use schemas.  #### Related guides  - [Manage bucket schemas](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/). - [Create a bucket with an explicit schema](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/create-bucket/#create-a-bucket-with-an-explicit-schema)
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str bucket_id: A bucket ID. Adds a schema for the specified bucket. (required)
        :param MeasurementSchemaCreateRequest measurement_schema_create_request: (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not await self._is_cloud_instance_async():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._create_measurement_schema_prepare(bucket_id, measurement_schema_create_request, **kwargs)  # noqa: E501

        return await self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchema',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _create_measurement_schema_prepare(self, bucket_id, measurement_schema_create_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['bucket_id', 'measurement_schema_create_request', 'org', 'org_id']  # noqa: E501
        self._check_operation_params('create_measurement_schema', all_params, local_var_params)
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in local_var_params or
                local_var_params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `create_measurement_schema`")  # noqa: E501
        # verify the required parameter 'measurement_schema_create_request' is set
        if ('measurement_schema_create_request' not in local_var_params or
                local_var_params['measurement_schema_create_request'] is None):
            raise ValueError("Missing the required parameter `measurement_schema_create_request` when calling `create_measurement_schema`")  # noqa: E501

        path_params = {}
        if 'bucket_id' in local_var_params:
            path_params['bucketID'] = local_var_params['bucket_id']  # noqa: E501

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        body_params = None
        if 'measurement_schema_create_request' in local_var_params:
            body_params = local_var_params['measurement_schema_create_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def get_measurement_schema(self, bucket_id, measurement_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a measurement schema.

        Retrieves an explicit measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_measurement_schema(bucket_id, measurement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Retrieves schemas for the specified bucket. (required)
        :param str measurement_id: The measurement schema ID. Specifies the measurement schema to retrieve. (required)
        :param str org: Organization name. Specifies the organization that owns the schema.
        :param str org_id: Organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_measurement_schema_with_http_info(bucket_id, measurement_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_measurement_schema_with_http_info(bucket_id, measurement_id, **kwargs)  # noqa: E501
            return data

    def get_measurement_schema_with_http_info(self, bucket_id, measurement_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a measurement schema.

        Retrieves an explicit measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_measurement_schema_with_http_info(bucket_id, measurement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Retrieves schemas for the specified bucket. (required)
        :param str measurement_id: The measurement schema ID. Specifies the measurement schema to retrieve. (required)
        :param str org: Organization name. Specifies the organization that owns the schema.
        :param str org_id: Organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not self._is_cloud_instance():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_measurement_schema_prepare(bucket_id, measurement_id, **kwargs)  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements/{measurementID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchema',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_measurement_schema_async(self, bucket_id, measurement_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a measurement schema.

        Retrieves an explicit measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema).
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str bucket_id: A bucket ID. Retrieves schemas for the specified bucket. (required)
        :param str measurement_id: The measurement schema ID. Specifies the measurement schema to retrieve. (required)
        :param str org: Organization name. Specifies the organization that owns the schema.
        :param str org_id: Organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not await self._is_cloud_instance_async():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_measurement_schema_prepare(bucket_id, measurement_id, **kwargs)  # noqa: E501

        return await self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements/{measurementID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchema',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_measurement_schema_prepare(self, bucket_id, measurement_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['bucket_id', 'measurement_id', 'org', 'org_id']  # noqa: E501
        self._check_operation_params('get_measurement_schema', all_params, local_var_params)
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in local_var_params or
                local_var_params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `get_measurement_schema`")  # noqa: E501
        # verify the required parameter 'measurement_id' is set
        if ('measurement_id' not in local_var_params or
                local_var_params['measurement_id'] is None):
            raise ValueError("Missing the required parameter `measurement_id` when calling `get_measurement_schema`")  # noqa: E501

        path_params = {}
        if 'bucket_id' in local_var_params:
            path_params['bucketID'] = local_var_params['bucket_id']  # noqa: E501
        if 'measurement_id' in local_var_params:
            path_params['measurementID'] = local_var_params['measurement_id']  # noqa: E501

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def get_measurement_schemas(self, bucket_id, **kwargs):  # noqa: E501,D401,D403
        """List measurement schemas of a bucket.

        Lists _explicit_ [schemas](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema) (`"schemaType": "explicit"`) for a bucket.  _Explicit_ schemas are used to enforce column names, tags, fields, and data types for your data.  By default, buckets have an _implicit_ schema-type (`"schemaType": "implicit"`) that conforms to your data.  #### Related guides  - [Using bucket schemas](https://www.influxdata.com/blog/new-bucket-schema-option-protect-from-unwanted-schema-changes/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_measurement_schemas(bucket_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Lists measurement schemas for the specified bucket. (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :param str name: A measurement name. Only returns measurement schemas with the specified name.
        :return: MeasurementSchemaList
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_measurement_schemas_with_http_info(bucket_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_measurement_schemas_with_http_info(bucket_id, **kwargs)  # noqa: E501
            return data

    def get_measurement_schemas_with_http_info(self, bucket_id, **kwargs):  # noqa: E501,D401,D403
        """List measurement schemas of a bucket.

        Lists _explicit_ [schemas](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema) (`"schemaType": "explicit"`) for a bucket.  _Explicit_ schemas are used to enforce column names, tags, fields, and data types for your data.  By default, buckets have an _implicit_ schema-type (`"schemaType": "implicit"`) that conforms to your data.  #### Related guides  - [Using bucket schemas](https://www.influxdata.com/blog/new-bucket-schema-option-protect-from-unwanted-schema-changes/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_measurement_schemas_with_http_info(bucket_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Lists measurement schemas for the specified bucket. (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :param str name: A measurement name. Only returns measurement schemas with the specified name.
        :return: MeasurementSchemaList
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not self._is_cloud_instance():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_measurement_schemas_prepare(bucket_id, **kwargs)  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchemaList',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_measurement_schemas_async(self, bucket_id, **kwargs):  # noqa: E501,D401,D403
        """List measurement schemas of a bucket.

        Lists _explicit_ [schemas](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema) (`"schemaType": "explicit"`) for a bucket.  _Explicit_ schemas are used to enforce column names, tags, fields, and data types for your data.  By default, buckets have an _implicit_ schema-type (`"schemaType": "implicit"`) that conforms to your data.  #### Related guides  - [Using bucket schemas](https://www.influxdata.com/blog/new-bucket-schema-option-protect-from-unwanted-schema-changes/)
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str bucket_id: A bucket ID. Lists measurement schemas for the specified bucket. (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :param str name: A measurement name. Only returns measurement schemas with the specified name.
        :return: MeasurementSchemaList
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not await self._is_cloud_instance_async():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_measurement_schemas_prepare(bucket_id, **kwargs)  # noqa: E501

        return await self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchemaList',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_measurement_schemas_prepare(self, bucket_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['bucket_id', 'org', 'org_id', 'name']  # noqa: E501
        self._check_operation_params('get_measurement_schemas', all_params, local_var_params)
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in local_var_params or
                local_var_params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `get_measurement_schemas`")  # noqa: E501

        path_params = {}
        if 'bucket_id' in local_var_params:
            path_params['bucketID'] = local_var_params['bucket_id']  # noqa: E501

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501

        header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def update_measurement_schema(self, bucket_id, measurement_id, measurement_schema_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a measurement schema.

        Updates a measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema).  Use this endpoint to update the fields (`name`, `type`, and `dataType`) of a measurement schema.  #### Limitations  - You can't update the `name` of a measurement.  #### Related guides  - [Manage bucket schemas](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/). - [Using bucket schemas](https://www.influxdata.com/blog/new-bucket-schema-option-protect-from-unwanted-schema-changes/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_measurement_schema(bucket_id, measurement_id, measurement_schema_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Specifies the bucket to retrieve schemas for. (required)
        :param str measurement_id: A measurement schema ID. Retrieves the specified measurement schema. (required)
        :param MeasurementSchemaUpdateRequest measurement_schema_update_request: (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_measurement_schema_with_http_info(bucket_id, measurement_id, measurement_schema_update_request, **kwargs)  # noqa: E501
        else:
            (data) = self.update_measurement_schema_with_http_info(bucket_id, measurement_id, measurement_schema_update_request, **kwargs)  # noqa: E501
            return data

    def update_measurement_schema_with_http_info(self, bucket_id, measurement_id, measurement_schema_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a measurement schema.

        Updates a measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema).  Use this endpoint to update the fields (`name`, `type`, and `dataType`) of a measurement schema.  #### Limitations  - You can't update the `name` of a measurement.  #### Related guides  - [Manage bucket schemas](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/). - [Using bucket schemas](https://www.influxdata.com/blog/new-bucket-schema-option-protect-from-unwanted-schema-changes/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_measurement_schema_with_http_info(bucket_id, measurement_id, measurement_schema_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bucket_id: A bucket ID. Specifies the bucket to retrieve schemas for. (required)
        :param str measurement_id: A measurement schema ID. Retrieves the specified measurement schema. (required)
        :param MeasurementSchemaUpdateRequest measurement_schema_update_request: (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not self._is_cloud_instance():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._update_measurement_schema_prepare(bucket_id, measurement_id, measurement_schema_update_request, **kwargs)  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements/{measurementID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchema',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def update_measurement_schema_async(self, bucket_id, measurement_id, measurement_schema_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a measurement schema.

        Updates a measurement [schema](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#schema).  Use this endpoint to update the fields (`name`, `type`, and `dataType`) of a measurement schema.  #### Limitations  - You can't update the `name` of a measurement.  #### Related guides  - [Manage bucket schemas](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/). - [Using bucket schemas](https://www.influxdata.com/blog/new-bucket-schema-option-protect-from-unwanted-schema-changes/).
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str bucket_id: A bucket ID. Specifies the bucket to retrieve schemas for. (required)
        :param str measurement_id: A measurement schema ID. Retrieves the specified measurement schema. (required)
        :param MeasurementSchemaUpdateRequest measurement_schema_update_request: (required)
        :param str org: An organization name. Specifies the organization that owns the schema.
        :param str org_id: An organization ID. Specifies the organization that owns the schema.
        :return: MeasurementSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        if not await self._is_cloud_instance_async():
            from influxdb_client_python_boost.client.warnings import CloudOnlyWarning
            CloudOnlyWarning.print_warning('BucketSchemasService',
                                           'https://docs.influxdata.com/influxdb/cloud/organizations/buckets/bucket-schema/')  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._update_measurement_schema_prepare(bucket_id, measurement_id, measurement_schema_update_request, **kwargs)  # noqa: E501

        return await self.api_client.call_api(
            '/api/v2/buckets/{bucketID}/schema/measurements/{measurementID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='MeasurementSchema',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _update_measurement_schema_prepare(self, bucket_id, measurement_id, measurement_schema_update_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['bucket_id', 'measurement_id', 'measurement_schema_update_request', 'org', 'org_id']  # noqa: E501
        self._check_operation_params('update_measurement_schema', all_params, local_var_params)
        # verify the required parameter 'bucket_id' is set
        if ('bucket_id' not in local_var_params or
                local_var_params['bucket_id'] is None):
            raise ValueError("Missing the required parameter `bucket_id` when calling `update_measurement_schema`")  # noqa: E501
        # verify the required parameter 'measurement_id' is set
        if ('measurement_id' not in local_var_params or
                local_var_params['measurement_id'] is None):
            raise ValueError("Missing the required parameter `measurement_id` when calling `update_measurement_schema`")  # noqa: E501
        # verify the required parameter 'measurement_schema_update_request' is set
        if ('measurement_schema_update_request' not in local_var_params or
                local_var_params['measurement_schema_update_request'] is None):
            raise ValueError("Missing the required parameter `measurement_schema_update_request` when calling `update_measurement_schema`")  # noqa: E501

        path_params = {}
        if 'bucket_id' in local_var_params:
            path_params['bucketID'] = local_var_params['bucket_id']  # noqa: E501
        if 'measurement_id' in local_var_params:
            path_params['measurementID'] = local_var_params['measurement_id']  # noqa: E501

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        body_params = None
        if 'measurement_schema_update_request' in local_var_params:
            body_params = local_var_params['measurement_schema_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
