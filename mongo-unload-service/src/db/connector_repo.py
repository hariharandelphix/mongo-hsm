#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.db.connection import get_db
from src.models.connector import Connector


class ConnectorRepository:
    """
    Connector repository class responsible for all
    DB operations related to connector
    """

    def __init__(self) -> None:
        self.db: Session = get_db().__next__()

    async def create(self, payload: dict):
        try:
            new_connector = Connector(**payload)
            self.db.add(new_connector)
            self.db.commit()
            self.db.refresh(new_connector)
            return new_connector
        except IntegrityError:
            self.db.rollback()

    def get_by_id(self, _id: str):
        return self.db.query(Connector).filter(Connector.id == _id).first()

    def get_all(self):
        connectors = self.db.query(Connector).all()
        return connectors

    # async def delete(self,item_id: str):
    #     db_item= self.db.query(models.Task).filter_by(id=item_id).first()
    #     self.db.delete(db_item)
    #     self.db.commit()

    # async def update(self, item_data):
    #     updated_item = self.db.merge(item_data)
    #     self.db.commit()
    #     return updated_item


connector_repo = ConnectorRepository()
