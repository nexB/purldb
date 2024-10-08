#
# Copyright (c) nexB Inc. and others. All rights reserved.
# purldb is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/aboutcode-org/purldb for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


import os

from django.test import TestCase as DjangoTestCase

from packagedcode import models as scan_models

from minecode import utils
from minecode.utils_test import JsonBasedTesting


class UtilsTest(JsonBasedTesting, DjangoTestCase):
    test_data_dir = os.path.join(os.path.dirname(__file__), "testfiles")

    def test_stringify_null_purl_fields_with_missing_purl_fields(self):
        common_data = {"type": None}

        utils.stringify_null_purl_fields(common_data)

        self.assertEqual(1, len(common_data))
        self.assertEqual("", common_data["type"])

    def test_stringify_null_purl_fields(self):
        common_data = {
            "type": None,
            "namespace": None,
            "name": None,
            "version": None,
            "qualifiers": None,
            "subpath": None,
        }

        utils.stringify_null_purl_fields(common_data)

        for d in common_data:
            self.assertIsNotNone(common_data[d])
            self.assertEqual("", common_data[d])

    def test_set_purl(self):
        common_data = dict(
            type="generic",
            name="openssl",
            description="The OpenSSL Project is a collaborative effort.",
        )
        package = scan_models.Package(**common_data)
        package.set_purl("pkg:generic/openssl@1.0.2o")
        self.assertEqual(None, package.namespace)
        self.assertEqual("generic", package.type)
        self.assertEqual("openssl", package.name)
        self.assertEqual("1.0.2o", package.version)
        self.assertEqual({}, package.qualifiers)
        self.assertEqual(None, package.subpath)

    def test_is_int(self):
        self.assertTrue(utils.is_int(0))
        self.assertFalse(utils.is_int("a"))

    def test_validate_uuid(self):
        invalid_uuid1 = "invalid"
        invalid_uuid2 = "123e4567-e89b-12d3-a456-42665544000G"
        valid_uuid = "c2cf7ef0-d3be-4011-bda7-8eb4a196eef2"

        for uuid, expected_result in [
            [invalid_uuid1, False],
            [invalid_uuid2, False],
            [valid_uuid, True],
        ]:
            self.assertEqual(expected_result, utils.validate_uuid(uuid))
