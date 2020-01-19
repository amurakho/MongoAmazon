import amazon_models


class DirtyMongoManage:

    def __init__(self, url):
        self.url = url
        try:
            self.dirty_mongo = amazon_models.DirtyMongo.objects.get(url=url)
        except Exception as e:
            self.dirty_mongo = amazon_models.DirtyMongo.objects.create(url=url)

    def set_main(self, data):
        for key, value in data.items():
            if self.dirty_mongo.description and key == 'description':
                value = ' '.join([self.dirty_mongo.description, value])
            setattr(self.dirty_mongo, key, value)
        self.dirty_mongo.save()

    def set_category(self, categories):
        for category in categories:
            if not category or category in self.dirty_mongo.category:
                continue
            self.dirty_mongo.category.append(category)
        self.dirty_mongo.save()


class ClearlyMongoManage:

    pass
