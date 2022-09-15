import pymongo
from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    COLLECTION = "feira_livres"
    primary_index_fields = {"registro"}

    @property
    def collection_name(self):
        return self.db[self.COLLECTION]

    def upgrade(self):
        try:
            self.db.create_collection(self.COLLECTION)
        except Exception:
            pass
        
        self.create_primary_key()

    def downgrade(self):
        self.db.drop_collection(self.COLLECTION)

    def create_primary_key(self):
        self.collection_name.create_index(
          [(key, pymongo.ASCENDING) for key in self.primary_index_fields],
          unique=True,
          name="primary_key",
        ) 
