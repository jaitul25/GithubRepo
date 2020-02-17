"""Test cases for fetching repository"""

import unittest
from HW04a_Jaitul_Bharodiya import get_repo_details

class TestRepo(unittest.TestCase):
    """Test the Repos"""
    def test_repos(self):
        """Testing the repository and commits"""
        self.assertEqual(get_repo_details('themalavshastri'),['User: themalavshastri','Repo: Algorithms- Number of commits: 2','Repo: MachineLearning Number of commits: 1'])


if __name__ == '__main__':
    unittest.main()
