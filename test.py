import unittest
from MongoManage import DirtyMongoManage
import amazon_models
import mongoengine


class DirtyMongoTest(unittest.TestCase):
    def setUp(self) -> None:
        mongoengine.connect(db='dirty_amazon',
                            username='Artem Murakhovskyi', host='localhost', port=27017)
        self.url = 'https://www.testurl.com'

    def _get_data(self):
        tested_object = amazon_models.DirtyMongo.objects.get(url=self.url)
        tested_data = {
            'description': tested_object.description,
            'asin': tested_object.asin,
            'category': tested_object.category
        }
        return tested_data

    def test_new_data(self):
        dirty_manage = DirtyMongoManage(self.url)
        data = {
            'description': 'some new description',
            'asin': '1234567',
        }
        categories = ['test_category']
        dirty_manage.set_main(data)
        dirty_manage.set_category(categories)

        checking_data = {
            'description': 'some new description',
            'asin': '1234567',
            'category': ['test_category']
        }
        tested_data = self._get_data()
        self.assertEqual(checking_data, tested_data)

    def test_update_descr(self):
        dirty_manage = DirtyMongoManage(self.url)
        data = {
            'description': 'first part of description',
            'asin': '1234567',
        }
        categories = ['test category']
        dirty_manage.set_main(data)
        dirty_manage.set_category(categories)

        updated_data = {
            'description': 'second part of description',
            'asin': '7654321',
        }
        categories = [None, 'second category']
        dirty_manage.set_main(updated_data)
        dirty_manage.set_category(categories)

        checked_data = {
            'description': 'first part of description second part of description',
            'asin': '7654321',
            'category': ['test category', 'second category']
        }
        tested_data = self._get_data()
        self.assertEqual(checked_data, tested_data)

    def tearDown(self) -> None:
        amazon_models.DirtyMongo.objects.get(url=self.url).delete()


if __name__ == '__main__':
    unittest.main()
