import unittest
from click.testing import CliRunner
from b3notify import B3Notify, cli


class TestB3Notify(unittest.TestCase):

    def setUp(self):
        self.notify = B3Notify()
        self.notify.read_configuration()
        self.runner = CliRunner()

    def test_config(self):
        notify = B3Notify()
        notify.read_configuration()
        self.assertEqual(notify.username, 'test')
        self.assertEqual(notify.password, 'test123')
        self.assertEqual(
            notify.url,
            'https://bitbucket.pearson.com/rest/build-status/1.0/commits/'
        )
        self.assertEqual('dGVzdDp0ZXN0MTIz', notify.auth)

    def test_cli_1(self):
        result = self.runner.invoke(
            cli, [
                '--success', '--commit=abc', '-b=http://localhost',
                '-k=build-key', '-n=build-name'])
        self.assertEqual(-1, result.exit_code)

    def test_headers(self):
        self.assertTrue(
            'Content-Type' in self.notify.headers)
        self.assertTrue(
            'Authorization' in self.notify.headers)
        headers = self.notify.headers
        self.assertEqual(headers['Content-Type'], 'application/json')
        self.assertEqual(headers['Authorization'], 'Basic dGVzdDp0ZXN0MTIz')
