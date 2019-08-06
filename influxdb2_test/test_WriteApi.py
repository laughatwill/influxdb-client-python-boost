# coding: utf-8

from __future__ import absolute_import

import datetime
import unittest
from multiprocessing.pool import ApplyResult

from influxdb2 import WritePrecision
from influxdb2.client.write_api import SYNCHRONOUS, ASYNCHRONOUS
from influxdb2_test.base_test import BaseTest


class SynchronousWriteTest(BaseTest):

    def setUp(self) -> None:
        super().setUp()
        self.write_client = self.client.write_api(write_options=SYNCHRONOUS)

    def tearDown(self) -> None:
        self.write_client.__del__()
        super().tearDown()

    def test_write_line_protocol(self):
        bucket = self.create_test_bucket()

        record = "h2o_feet,location=coyote_creek level\\ water_level=1.0 1"
        self.write_client.write(bucket.name, self.org, record)
        self.write_client.flush()

        result = self.query_client.query(
            "from(bucket:\"" + bucket.name + "\") |> range(start: 1970-01-01T00:00:00.000000001Z) |> last()", self.org)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].records[0].get_measurement(), "h2o_feet")
        self.assertEqual(result[0].records[0].get_value(), 1.0)
        self.assertEqual(result[0].records[0].get_field(), "level water_level")
        self.assertEqual(result[0].records[0].get_time(),
                         datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc))

        self.delete_test_bucket(bucket)

    #####################################

    def test_write_precision(self):
        bucket = self.create_test_bucket()

        self.write_client.write(org="my-org", bucket=bucket.name, record="air,location=Python humidity=99",
                                write_precision=WritePrecision.MS)

        result = self.query_client.query(
            "from(bucket:\"" + bucket.name + "\") |> range(start: 1970-01-01T00:00:00.000000001Z) |> last()", self.org)

        self.assertEqual(len(result), 1)

        self.delete_test_bucket(bucket)

    def test_write_records_list(self):
        bucket = self.create_test_bucket()

        _record1 = "h2o_feet,location=coyote_creek level\\ water_level=1.0 1"
        _record2 = "h2o_feet,location=coyote_creek level\\ water_level=2.0 2"

        record_list = [_record1, _record2]

        self.write_client.write(bucket.name, self.org, record_list)

        self.write_client.flush()

        query = 'from(bucket:"' + bucket.name + '") |> range(start: 1970-01-01T00:00:00.000000001Z)'
        print(query)

        flux_result = self.client.query_api().query(query)

        self.assertEqual(1, len(flux_result))

        records = flux_result[0].records

        self.assertEqual(2, len(records))

        self.assertEqual("h2o_feet", records[0].get_measurement())
        self.assertEqual(1, records[0].get_value())
        self.assertEqual("level water_level", records[0].get_field())

        self.assertEqual("h2o_feet", records[1].get_measurement())
        self.assertEqual(2, records[1].get_value())
        self.assertEqual("level water_level", records[1].get_field())

    def test_write_result(self):

        _bucket = self.create_test_bucket()

        _record = "h2o_feet,location=coyote_creek level\\ water_level=1.0 1"
        result = self.write_client.write(_bucket.name, self.org, _record)

        # The success response is 204 - No Content
        self.assertEqual(None, result)


class AsynchronousWriteTest(BaseTest):

    def setUp(self) -> None:
        super().setUp()
        self.write_client = self.client.write_api(write_options=ASYNCHRONOUS)

    def tearDown(self) -> None:
        self.write_client.__del__()
        super().tearDown()

    def test_write_result(self):
        _bucket = self.create_test_bucket()

        _record = "h2o_feet,location=coyote_creek level\\ water_level=1.0 1"
        result = self.write_client.write(_bucket.name, self.org, _record)

        self.assertEqual(ApplyResult, type(result))
        self.assertEqual(None, result.get())


if __name__ == '__main__':
    unittest.main()
