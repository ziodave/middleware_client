# coding: utf-8

"""
    Middleware

    Knowledge Graph data management.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from middleware_client.models.batch_request import BatchRequest

class TestBatchRequest(unittest.TestCase):
    """BatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchRequest:
        """Test BatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchRequest`
        """
        model = BatchRequest()
        if include_optional:
            return BatchRequest(
                uri = '',
                model = '',
                private = True
            )
        else:
            return BatchRequest(
                uri = '',
                model = '',
        )
        """

    def testBatchRequest(self):
        """Test BatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
