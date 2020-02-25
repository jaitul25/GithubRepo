"""Test cases for fetching repository"""

import unittest
import json
from unittest import mock
from HW04a_Jaitul_Bharodiya import get_repo_details


def get_url(url):
    if url == "https://api.github.com/users/themalavshastri/repos":
        return fetch_repo('rep.json')

class content:
    content = ''
    
def fetch_repo(loc):
    data = content()
    with open(loc,'r') as f:
        data.content = json.loads(f)
    return data.content


class TestRepo(unittest.TestCase):
    """Test the Repos"""

    @mock.patch('requests.get')
    def test_repos(self,mocked):
        """Testing the repository and commits"""
        mocked.side_effect = get_url
        reposit = get_repo_details('themalavshastri')
        self.assertEqual(reposit,"unable to fetch user's repos")



if __name__ == '__main__':
    unittest.main()
