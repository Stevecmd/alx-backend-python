#!/usr/bin/env python3
""" Test client module """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test GithubOrgClient"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch(
        'client.get_json',
        return_value={"repos_url": "https://api.github.com/orgs/google/repos"}
    )
    def test_org(self, org_name, expected, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test/repos"
            }
            client = GithubOrgClient("test")
            expected = "https://api.github.com/orgs/test/repos"
            self.assertEqual(
                client._public_repos_url,
                expected
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method

        Args:
            mock_get_json: Mocked get_json function
        """
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test/repos"
        ) as mock_public_repos_url:
            client = GithubOrgClient("test")
            repos = client.public_repos()

            # Test the list of repos is correct
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)

            # Test that mocked property was called once
            mock_public_repos_url.assert_called_once()

            # Test that mocked get_json was called once with correct URL
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit-test for GithubOrgClient.has_license

        Args:
            repo: Dictionary representing a repository
            license_key: License key to check for
            expected: Expected return value
        """
        client = GithubOrgClient("test")
        has_license = client.has_license(repo, license_key)
        self.assertEqual(has_license, expected)


if __name__ == '__main__':
    unittest.main()
