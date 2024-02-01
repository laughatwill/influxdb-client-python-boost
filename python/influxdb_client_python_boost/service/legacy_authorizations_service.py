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


class LegacyAuthorizationsService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """LegacyAuthorizationsService - a operation defined in OpenAPI."""
        super().__init__(api_client)

    def delete_legacy_authorizations_id(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_legacy_authorizations_id(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_legacy_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_legacy_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
            return data

    def delete_legacy_authorizations_id_with_http_info(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_legacy_authorizations_id_with_http_info(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._delete_legacy_authorizations_id_prepare(auth_id, **kwargs)

        return self.api_client.call_api(
            '/private/legacy/authorizations/{authID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def delete_legacy_authorizations_id_async(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a legacy authorization.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._delete_legacy_authorizations_id_prepare(auth_id, **kwargs)

        return await self.api_client.call_api(
            '/private/legacy/authorizations/{authID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _delete_legacy_authorizations_id_prepare(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['auth_id', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('delete_legacy_authorizations_id', all_params, local_var_params)
        # verify the required parameter 'auth_id' is set
        if ('auth_id' not in local_var_params or
                local_var_params['auth_id'] is None):
            raise ValueError("Missing the required parameter `auth_id` when calling `delete_legacy_authorizations_id`")  # noqa: E501

        path_params = {}
        if 'auth_id' in local_var_params:
            path_params['authID'] = local_var_params['auth_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def get_legacy_authorizations(self, **kwargs):  # noqa: E501,D401,D403
        """List all legacy authorizations.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show legacy authorizations that belong to a user ID.
        :param str user: Only show legacy authorizations that belong to a user name.
        :param str org_id: Only show legacy authorizations that belong to an organization ID.
        :param str org: Only show legacy authorizations that belong to a organization name.
        :param str token: Only show legacy authorizations with a specified token (auth name).
        :param str auth_id: Only show legacy authorizations with a specified auth ID.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_legacy_authorizations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_legacy_authorizations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_legacy_authorizations_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """List all legacy authorizations.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show legacy authorizations that belong to a user ID.
        :param str user: Only show legacy authorizations that belong to a user name.
        :param str org_id: Only show legacy authorizations that belong to an organization ID.
        :param str org: Only show legacy authorizations that belong to a organization name.
        :param str token: Only show legacy authorizations with a specified token (auth name).
        :param str auth_id: Only show legacy authorizations with a specified auth ID.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_legacy_authorizations_prepare(**kwargs)

        return self.api_client.call_api(
            '/private/legacy/authorizations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorizations',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_legacy_authorizations_async(self, **kwargs):  # noqa: E501,D401,D403
        """List all legacy authorizations.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show legacy authorizations that belong to a user ID.
        :param str user: Only show legacy authorizations that belong to a user name.
        :param str org_id: Only show legacy authorizations that belong to an organization ID.
        :param str org: Only show legacy authorizations that belong to a organization name.
        :param str token: Only show legacy authorizations with a specified token (auth name).
        :param str auth_id: Only show legacy authorizations with a specified auth ID.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_legacy_authorizations_prepare(**kwargs)

        return await self.api_client.call_api(
            '/private/legacy/authorizations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorizations',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_legacy_authorizations_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span', 'user_id', 'user', 'org_id', 'org', 'token', 'auth_id']  # noqa: E501
        self._check_operation_params('get_legacy_authorizations', all_params, local_var_params)

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('userID', local_var_params['user_id']))  # noqa: E501
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'token' in local_var_params:
            query_params.append(('token', local_var_params['token']))  # noqa: E501
        if 'auth_id' in local_var_params:
            query_params.append(('authID', local_var_params['auth_id']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def get_legacy_authorizations_id(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations_id(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_legacy_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_legacy_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
            return data

    def get_legacy_authorizations_id_with_http_info(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations_id_with_http_info(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_legacy_authorizations_id_prepare(auth_id, **kwargs)

        return self.api_client.call_api(
            '/private/legacy/authorizations/{authID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorization',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_legacy_authorizations_id_async(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a legacy authorization.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_legacy_authorizations_id_prepare(auth_id, **kwargs)

        return await self.api_client.call_api(
            '/private/legacy/authorizations/{authID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorization',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_legacy_authorizations_id_prepare(self, auth_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['auth_id', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('get_legacy_authorizations_id', all_params, local_var_params)
        # verify the required parameter 'auth_id' is set
        if ('auth_id' not in local_var_params or
                local_var_params['auth_id'] is None):
            raise ValueError("Missing the required parameter `auth_id` when calling `get_legacy_authorizations_id`")  # noqa: E501

        path_params = {}
        if 'auth_id' in local_var_params:
            path_params['authID'] = local_var_params['auth_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def patch_legacy_authorizations_id(self, auth_id, authorization_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a legacy authorization to be active or inactive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_legacy_authorizations_id(auth_id, authorization_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Legacy authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_legacy_authorizations_id_with_http_info(auth_id, authorization_update_request, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_legacy_authorizations_id_with_http_info(auth_id, authorization_update_request, **kwargs)  # noqa: E501
            return data

    def patch_legacy_authorizations_id_with_http_info(self, auth_id, authorization_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a legacy authorization to be active or inactive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_legacy_authorizations_id_with_http_info(auth_id, authorization_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Legacy authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._patch_legacy_authorizations_id_prepare(auth_id, authorization_update_request, **kwargs)

        return self.api_client.call_api(
            '/private/legacy/authorizations/{authID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorization',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def patch_legacy_authorizations_id_async(self, auth_id, authorization_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a legacy authorization to be active or inactive.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Legacy authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._patch_legacy_authorizations_id_prepare(auth_id, authorization_update_request, **kwargs)

        return await self.api_client.call_api(
            '/private/legacy/authorizations/{authID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorization',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _patch_legacy_authorizations_id_prepare(self, auth_id, authorization_update_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['auth_id', 'authorization_update_request', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('patch_legacy_authorizations_id', all_params, local_var_params)
        # verify the required parameter 'auth_id' is set
        if ('auth_id' not in local_var_params or
                local_var_params['auth_id'] is None):
            raise ValueError("Missing the required parameter `auth_id` when calling `patch_legacy_authorizations_id`")  # noqa: E501
        # verify the required parameter 'authorization_update_request' is set
        if ('authorization_update_request' not in local_var_params or
                local_var_params['authorization_update_request'] is None):
            raise ValueError("Missing the required parameter `authorization_update_request` when calling `patch_legacy_authorizations_id`")  # noqa: E501

        path_params = {}
        if 'auth_id' in local_var_params:
            path_params['authID'] = local_var_params['auth_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        if 'authorization_update_request' in local_var_params:
            body_params = local_var_params['authorization_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_legacy_authorizations(self, legacy_authorization_post_request, **kwargs):  # noqa: E501,D401,D403
        """Create a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations(legacy_authorization_post_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LegacyAuthorizationPostRequest legacy_authorization_post_request: Legacy authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_legacy_authorizations_with_http_info(legacy_authorization_post_request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_legacy_authorizations_with_http_info(legacy_authorization_post_request, **kwargs)  # noqa: E501
            return data

    def post_legacy_authorizations_with_http_info(self, legacy_authorization_post_request, **kwargs):  # noqa: E501,D401,D403
        """Create a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations_with_http_info(legacy_authorization_post_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LegacyAuthorizationPostRequest legacy_authorization_post_request: Legacy authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_legacy_authorizations_prepare(legacy_authorization_post_request, **kwargs)

        return self.api_client.call_api(
            '/private/legacy/authorizations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorization',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_legacy_authorizations_async(self, legacy_authorization_post_request, **kwargs):  # noqa: E501,D401,D403
        """Create a legacy authorization.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param LegacyAuthorizationPostRequest legacy_authorization_post_request: Legacy authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_legacy_authorizations_prepare(legacy_authorization_post_request, **kwargs)

        return await self.api_client.call_api(
            '/private/legacy/authorizations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Authorization',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_legacy_authorizations_prepare(self, legacy_authorization_post_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['legacy_authorization_post_request', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('post_legacy_authorizations', all_params, local_var_params)
        # verify the required parameter 'legacy_authorization_post_request' is set
        if ('legacy_authorization_post_request' not in local_var_params or
                local_var_params['legacy_authorization_post_request'] is None):
            raise ValueError("Missing the required parameter `legacy_authorization_post_request` when calling `post_legacy_authorizations`")  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        if 'legacy_authorization_post_request' in local_var_params:
            body_params = local_var_params['legacy_authorization_post_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_legacy_authorizations_id_password(self, auth_id, password_reset_body, **kwargs):  # noqa: E501,D401,D403
        """Set a legacy authorization password.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations_id_password(auth_id, password_reset_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param PasswordResetBody password_reset_body: New password (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_legacy_authorizations_id_password_with_http_info(auth_id, password_reset_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_legacy_authorizations_id_password_with_http_info(auth_id, password_reset_body, **kwargs)  # noqa: E501
            return data

    def post_legacy_authorizations_id_password_with_http_info(self, auth_id, password_reset_body, **kwargs):  # noqa: E501,D401,D403
        """Set a legacy authorization password.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations_id_password_with_http_info(auth_id, password_reset_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param PasswordResetBody password_reset_body: New password (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_legacy_authorizations_id_password_prepare(auth_id, password_reset_body, **kwargs)

        return self.api_client.call_api(
            '/private/legacy/authorizations/{authID}/password', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_legacy_authorizations_id_password_async(self, auth_id, password_reset_body, **kwargs):  # noqa: E501,D401,D403
        """Set a legacy authorization password.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param PasswordResetBody password_reset_body: New password (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_legacy_authorizations_id_password_prepare(auth_id, password_reset_body, **kwargs)

        return await self.api_client.call_api(
            '/private/legacy/authorizations/{authID}/password', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_legacy_authorizations_id_password_prepare(self, auth_id, password_reset_body, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['auth_id', 'password_reset_body', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('post_legacy_authorizations_id_password', all_params, local_var_params)
        # verify the required parameter 'auth_id' is set
        if ('auth_id' not in local_var_params or
                local_var_params['auth_id'] is None):
            raise ValueError("Missing the required parameter `auth_id` when calling `post_legacy_authorizations_id_password`")  # noqa: E501
        # verify the required parameter 'password_reset_body' is set
        if ('password_reset_body' not in local_var_params or
                local_var_params['password_reset_body'] is None):
            raise ValueError("Missing the required parameter `password_reset_body` when calling `post_legacy_authorizations_id_password`")  # noqa: E501

        path_params = {}
        if 'auth_id' in local_var_params:
            path_params['authID'] = local_var_params['auth_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        if 'password_reset_body' in local_var_params:
            body_params = local_var_params['password_reset_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
