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


class SetupService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """SetupService - a operation defined in OpenAPI."""
        super().__init__(api_client)

    def get_setup(self, **kwargs):  # noqa: E501,D401,D403
        """Check if database has default user, org, bucket.

        Returns `true` if no default user, organization, or bucket has been created.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_setup(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: IsOnboarding
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_setup_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_setup_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_setup_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Check if database has default user, org, bucket.

        Returns `true` if no default user, organization, or bucket has been created.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_setup_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: IsOnboarding
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_setup_prepare(**kwargs)  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/setup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='IsOnboarding',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_setup_async(self, **kwargs):  # noqa: E501,D401,D403
        """Check if database has default user, org, bucket.

        Returns `true` if no default user, organization, or bucket has been created.
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: IsOnboarding
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_setup_prepare(**kwargs)  # noqa: E501

        return await self.api_client.call_api(
            '/api/v2/setup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='IsOnboarding',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_setup_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span']  # noqa: E501
        self._check_operation_params('get_setup', all_params, local_var_params)

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_setup(self, onboarding_request, **kwargs):  # noqa: E501,D401,D403
        """Set up initial user, org and bucket.

        Post an onboarding request to set up initial user, org and bucket.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_setup(onboarding_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OnboardingRequest onboarding_request: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: OnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_setup_with_http_info(onboarding_request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_setup_with_http_info(onboarding_request, **kwargs)  # noqa: E501
            return data

    def post_setup_with_http_info(self, onboarding_request, **kwargs):  # noqa: E501,D401,D403
        """Set up initial user, org and bucket.

        Post an onboarding request to set up initial user, org and bucket.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_setup_with_http_info(onboarding_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OnboardingRequest onboarding_request: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: OnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_setup_prepare(onboarding_request, **kwargs)  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/setup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='OnboardingResponse',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_setup_async(self, onboarding_request, **kwargs):  # noqa: E501,D401,D403
        """Set up initial user, org and bucket.

        Post an onboarding request to set up initial user, org and bucket.
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param OnboardingRequest onboarding_request: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: OnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_setup_prepare(onboarding_request, **kwargs)  # noqa: E501

        return await self.api_client.call_api(
            '/api/v2/setup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='OnboardingResponse',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_setup_prepare(self, onboarding_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['onboarding_request', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('post_setup', all_params, local_var_params)
        # verify the required parameter 'onboarding_request' is set
        if ('onboarding_request' not in local_var_params or
                local_var_params['onboarding_request'] is None):
            raise ValueError("Missing the required parameter `onboarding_request` when calling `post_setup`")  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        if 'onboarding_request' in local_var_params:
            body_params = local_var_params['onboarding_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
