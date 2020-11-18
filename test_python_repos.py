import unittest
import python_repos


class Tests(unittest.TestCase):

    def testReposStatusCode(self):
        self.assertEqual(python_repos.r.status_code, 200)

    def testRepositoriesReturned(self):
        self.assertEqual(30,len(python_repos.repo_dicts))

    def testTotalRepositories(self):
        self.assertGreater(python_repos.response_dict['total_count'], 600000)




if __name__ == '__main__':
    unittest.main()
