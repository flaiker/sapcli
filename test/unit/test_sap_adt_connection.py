#!/usr/bin/env python3

import unittest
from unittest.mock import Mock, patch

import sap.adt
import sap.adt.errors

from fixtures_adt import ERROR_XML_PACKAGE_ALREADY_EXISTS

class TestADTConnection(unittest.TestCase):
    """Connection(host, client, user, password, port=None, ssl=True)"""

    def setUp(self):
        self.connection = sap.adt.Connection('example.host.org', '123', 'SAP*', 'PASS')

    def test_adt_connection_init_default(self):
        connection = sap.adt.Connection('localhost', '357', 'anzeiger', 'password')

        self.assertEqual(connection.user, 'anzeiger')
        self.assertEqual(connection.uri, 'sap/bc/adt')
        self.assertEqual(connection._base_url, 'https://localhost:443/sap/bc/adt')
        self.assertEqual(connection._query_args, 'sap-client=357&saml2=disabled')

    def test_adt_connection_init_no_ssl(self):
        connection = sap.adt.Connection('localhost', '357', 'anzeiger', 'password', ssl=False)

        self.assertEqual(connection._base_url, 'http://localhost:80/sap/bc/adt')

    def test_adt_connection_init_ssl_own_port(self):
        connection = sap.adt.Connection('localhost', '357', 'anzeiger', 'password', port=44300)

        self.assertEqual(connection._base_url, 'https://localhost:44300/sap/bc/adt')

    def test_adt_connection_init_no_ssl_own_port(self):
        connection = sap.adt.Connection('localhost', '357', 'anzeiger', 'password', ssl=False, port=8000)

        self.assertEqual(connection._base_url, 'http://localhost:8000/sap/bc/adt')

    def test_handle_http_error_adt_exception(self):
        req = Mock()

        res = Mock()
        res.headers = {'content-type': 'application/xml'}
        res.text = ERROR_XML_PACKAGE_ALREADY_EXISTS

        with self.assertRaises(sap.adt.errors.ADTError):
            sap.adt.Connection._handle_http_error(req, res)

    def test_handle_http_error_random_xml(self):
        req = Mock()

        res = Mock()
        res.headers = {'content-type': 'application/xml'}
        res.text = '<?xml version="1.0" encoding="utf-8"><error>random failure</error>'

        with self.assertRaises(sap.adt.errors.HTTPRequestError):
            sap.adt.Connection._handle_http_error(req, res)

    def test_handle_http_error_plain_text(self):
        req = Mock()

        res = Mock()
        res.headers = {'content-type': 'plain/text'}
        res.text = 'arbitrary crash'

        with self.assertRaises(sap.adt.errors.HTTPRequestError):
            sap.adt.Connection._handle_http_error(req, res)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_content_type_no_headers(self, mock_exec, mock_session, mock_adt_url):
        self.connection.execute('GET', 'url', content_type='application/xml')

        mock_exec.assert_called_once_with('session', 'GET', 'url',
                                          params=None,
                                          headers={'Content-Type': 'application/xml'},
                                          body=None)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_content_type_with_headers(self, mock_exec, mock_session, mock_adt_url):
        self.connection.execute('GET', 'example',
                                headers={'Content-Type': 'text/plain'},
                                content_type='application/xml')

        mock_exec.assert_called_once_with('session', 'GET', 'url',
                                          params=None,
                                          headers={'Content-Type': 'application/xml'},
                                          body=None)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_accept_no_headers(self, mock_exec, mock_session, mock_adt_url):
        mock_exec.return_value = Mock()
        mock_exec.return_value.headers = {'Content-Type': 'application/xml'}

        self.connection.execute('GET', 'example',
                                accept='application/xml')

        mock_exec.assert_called_once_with('session', 'GET', 'url',
                                          params=None,
                                          headers={'Accept': 'application/xml'},
                                          body=None)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_accept_with_headers(self, mock_exec, mock_session, mock_adt_url):
        mock_exec.return_value = Mock()
        mock_exec.return_value.headers = {'Content-Type': 'application/xml'}

        self.connection.execute('GET', 'example',
                                headers={'Accept': 'text/plain'},
                                accept='application/xml')

        mock_exec.assert_called_once_with('session', 'GET', 'url',
                                          params=None,
                                          headers={'Accept': 'application/xml'},
                                          body=None)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_content_type_and_accept(self, mock_exec, mock_session, mock_adt_url):
        mock_exec.return_value = Mock()
        mock_exec.return_value.headers = {'Content-Type': 'application/xml'}

        self.connection.execute('GET', 'example',
                                content_type='application/json',
                                accept='application/xml')

        mock_exec.assert_called_once_with('session', 'GET', 'url',
                                          params=None,
                                          headers={'Accept': 'application/xml',
                                                   'Content-Type': 'application/json'},
                                          body=None)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_content_type_and_accept_with_headers(self, mock_exec, mock_session, mock_adt_url):
        mock_exec.return_value = Mock()
        mock_exec.return_value.headers = {'Content-Type': 'application/xml'}

        self.connection.execute('GET', 'example',
                                headers={'Accept': 'text/plain',
                                         'Content-Type': 'text/plain'},
                                content_type='application/json',
                                accept='application/xml')

        mock_exec.assert_called_once_with('session', 'GET', 'url',
                                          params=None,
                                          headers={'Accept': 'application/xml',
                                                   'Content-Type': 'application/json'},
                                          body=None)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_accept_list(self, mock_exec, mock_session, mock_adt_url):
        mock_exec.return_value = Mock()
        mock_exec.return_value.headers = {'Content-Type': 'application/json'}

        self.connection.execute('GET', 'example',
                                accept=['application/xml', 'application/json'])

        mock_exec.assert_called_once_with('session', 'GET', 'url',
                                          params=None,
                                          headers={'Accept': 'application/xml, application/json'},
                                          body=None)

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_accept_unmatched_string(self, mock_exec, mock_session, mock_adt_url):
        mock_exec.return_value = Mock()
        mock_exec.return_value.headers = {'Content-Type': 'application/json'}
        mock_exec.return_value.text = 'mock'

        with self.assertRaises(sap.adt.errors.UnexpectedResponseContent) as caught:
            self.connection.execute('GET', 'example',
                                    accept='application/xml')

        self.assertEqual(str(caught.exception),
                         'Unexpected Content-Type: application/json with: mock')

    @patch('sap.adt.core.Connection._build_adt_url', return_value='url')
    @patch('sap.adt.core.Connection._get_session', return_value='session')
    @patch('sap.adt.core.Connection._execute_with_session')
    def test_execute_accept_unmatched_list(self, mock_exec, mock_session, mock_adt_url):
        mock_exec.return_value = Mock()
        mock_exec.return_value.headers = {'Content-Type': 'text/plain'}
        mock_exec.return_value.text = 'mock'

        with self.assertRaises(sap.adt.errors.UnexpectedResponseContent) as caught:
            self.connection.execute('GET', 'example',
                                    accept=['application/xml', 'application/json'])

        self.assertEqual(str(caught.exception),
                         'Unexpected Content-Type: text/plain with: mock')


if __name__ == '__main__':
    unittest.main()
