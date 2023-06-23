# coding: utf-8
#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

import json

from sqlalchemy import Column, Integer, Text
from src.db.connection import Base


class Connector(Base):
    __tablename__ = "connector"

    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)

    def get_dict(self) -> dict:
        if self.data:
            data = json.loads(self.data)
            return {
                "id": self.id,
                "user": data["user"],
                "jdbc_url": data["jdbc_url"],
                "connection_properties": data["connection_properties"],
                "password": data["password"],
                "restoreSensitiveFields": data["restoreSensitiveFields"],
            }
        return {"id": self.id}
