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


class MetricsService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """MetricsService - a operation defined in OpenAPI."""
        super().__init__(api_client)

    def get_metrics(self, **kwargs):  # noqa: E501,D401,D403
        """Retrieve workload performance metrics.

        Returns metrics about the workload performance of an InfluxDB instance.  Use this endpoint to get performance, resource, and usage metrics.  #### Related guides  - For the list of metrics categories, see [InfluxDB OSS metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/). - Learn how to use InfluxDB to [scrape Prometheus metrics](https://docs.influxdata.com/influxdb/latest/write-data/developer-tools/scrape-prometheus-metrics/). - Learn how InfluxDB [parses the Prometheus exposition format](https://docs.influxdata.com/influxdb/latest/reference/prometheus-metrics/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_metrics_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Retrieve workload performance metrics.

        Returns metrics about the workload performance of an InfluxDB instance.  Use this endpoint to get performance, resource, and usage metrics.  #### Related guides  - For the list of metrics categories, see [InfluxDB OSS metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/). - Learn how to use InfluxDB to [scrape Prometheus metrics](https://docs.influxdata.com/influxdb/latest/write-data/developer-tools/scrape-prometheus-metrics/). - Learn how InfluxDB [parses the Prometheus exposition format](https://docs.influxdata.com/influxdb/latest/reference/prometheus-metrics/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_metrics_prepare(**kwargs)  # noqa: E501

        return self.api_client.call_api(
            '/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='str',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_metrics_async(self, **kwargs):  # noqa: E501,D401,D403
        """Retrieve workload performance metrics.

        Returns metrics about the workload performance of an InfluxDB instance.  Use this endpoint to get performance, resource, and usage metrics.  #### Related guides  - For the list of metrics categories, see [InfluxDB OSS metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/). - Learn how to use InfluxDB to [scrape Prometheus metrics](https://docs.influxdata.com/influxdb/latest/write-data/developer-tools/scrape-prometheus-metrics/). - Learn how InfluxDB [parses the Prometheus exposition format](https://docs.influxdata.com/influxdb/latest/reference/prometheus-metrics/).
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_metrics_prepare(**kwargs)  # noqa: E501

        return await self.api_client.call_api(
            '/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='str',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_metrics_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span']  # noqa: E501
        self._check_operation_params('get_metrics', all_params, local_var_params)

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
