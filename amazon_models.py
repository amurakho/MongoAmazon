import mongoengine
from datetime import datetime


class DirtyMongo(mongoengine.Document):
    """
    Here i save data from scrapy
    """

    asin = mongoengine.StringField()
    category = mongoengine.ListField(mongoengine.StringField())
    description = mongoengine.StringField()

    upload_date = mongoengine.DateTimeField()
    updated_date = mongoengine.DateTimeField()

    url = mongoengine.URLField()

    cleared = mongoengine.BinaryField()

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.upload_date = datetime.now()


class ClearlyMongo(mongoengine.Document):
    """
    Here i save data after clear it
    """
    pass
