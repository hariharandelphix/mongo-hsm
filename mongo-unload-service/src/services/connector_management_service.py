#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

import json
from typing import Union

from src.db.connector_repo import connector_repo
from src.models.connector import Connector


class ConnectorService:
    """
    Business logic for different connector operations
    """

    @staticmethod
    def get_all_connectors() -> list[Connector]:
        return connector_repo.get_all()

    @staticmethod
    async def create_connector(body: Connector) -> Union[None, Connector]:
        data = {}
        body = body.dict()
        data["id"] = body["id"]
        del body["id"]
        data["data"] = json.dumps(body)
        response = await connector_repo.create(data)
        return response
