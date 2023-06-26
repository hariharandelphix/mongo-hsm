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
    async def get_all_connectors() -> list[Connector]:
        return await connector_repo.get_all()

    @staticmethod
    async def get_connector_by_id(connector_id) -> Union[None, Connector]:
        return await connector_repo.get_by_id(connector_id)

    @staticmethod
    async def delete_connector_by_id(connector_id) -> Union[None, Connector]:
        return await connector_repo.delete(connector_id)

    @staticmethod
    async def create_connector(body: Connector) -> Union[None, Connector]:
        data = {}
        body = body.dict()
        data["id"] = body["id"]
        del body["id"]
        data["data"] = json.dumps(body)
        response = await connector_repo.create(data)
        return response

    @staticmethod
    async def update_connector(
        connector_id: str, body: Connector
    ) -> Union[None, Connector]:  # noqa
        data = {}
        body = body.dict()
        data["id"] = int(connector_id)
        del body["id"]
        data["data"] = json.dumps(body)
        response = await connector_repo.update(data)
        return response
