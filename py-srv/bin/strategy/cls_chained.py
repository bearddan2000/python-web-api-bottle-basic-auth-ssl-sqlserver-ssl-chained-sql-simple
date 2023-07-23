from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.sql import select, delete, insert, update, func

from model import DbModel

class Chained():
    def __init__(self, db: sessionmaker) -> None:
        self.db = db

    def jsonify_results(self, collection: ChunkedIteratorResult) -> dict:
        results = []
        for item in collection:
            for obj in item:
                results.append({
                    "id": obj.id,
                    "breed": obj.breed,
                    "color": obj.color
                })

        return {"results": results}

    def all(self):
        stm = select(DbModel)
        collection: ChunkedIteratorResult = self.db.execute(stm)
        return self.jsonify_results(collection)
        
    def commit_refresh(self, stm, args: dict=None) -> dict:
        if args is not None:
            self.db.execute(statement=stm,params=args)
        else:
            self.db.execute(statement=stm)
        self.db.commit()
        return self.all()
    
    def filter_by(self, dog_id):
        stm = select(DbModel).where(DbModel.id == dog_id)
        collection: ChunkedIteratorResult = self.db.execute(statement=stm)
        return self.jsonify_results(collection)

    def delete_by(self, dog_id):
        args = {"dog_id": int(dog_id)}
        stm = delete(DbModel).where(DbModel.id == dog_id)
        return self.commit_refresh(stm,args)

    def insert_last(self, dog_breed, dog_color):
        stm = select(func.max(DbModel.id))
        collection: ChunkedIteratorResult = self.db.execute(statement=stm)
        dog_id = 0
        for item in collection:
            for obj in item:
                dog_id = int(obj) + 1
        stm = insert(DbModel).values(id=dog_id, breed=dog_breed,color=dog_color)
        return self.commit_refresh(stm)

    def insert_entry(self, dog_breed, dog_color):
        self.insert_last(dog_breed, dog_color)
        return self.all()

    def update_entry(self, dog_id, dog_breed, dog_color):
        stm = update(DbModel) \
            .where(DbModel.id == dog_id) \
            .values(breed=dog_breed,color=dog_color)
        return self.commit_refresh(stm)
