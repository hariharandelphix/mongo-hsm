#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import List, Union

from fastapi import APIRouter, HTTPException, Path
from pydantic import conint
from src.services.connector_management_service import ConnectorService
from src.validators.connector_validator import Connector, ConnectorResponse
from starlette import status

router = APIRouter(
    prefix="/connectors",
    tags=["ConnectorManagement"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "",
    response_model=None,
    responses={"201": {"model": ConnectorResponse}},
    status_code=status.HTTP_201_CREATED,
)
async def create_connector(body: Connector) -> Union[None, ConnectorResponse]:  # noqa
    """
    Create Connector.
    """
    resp = await ConnectorService.create_connector(body)
    if resp:
        return ConnectorResponse(**resp.get_dict())
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Database Integrity Error",  # noqa
    )


@router.get(
    "",
    response_model=List[ConnectorResponse],
)
def list_all_connector() -> List[ConnectorResponse]:
    """
    Returns a list of connectors.
    """
    connectors = ConnectorService.get_all_connectors()
    return [ConnectorResponse(**i.get_dict()) for i in connectors]


@router.get(
    "/{connector_id}",
    response_model=ConnectorResponse,
)
def get_connector(
    connector_id: conint(ge=1) = Path(..., alias="connectorId")
) -> ConnectorResponse:
    """
    Get connector by Id.
    """
    connector = ConnectorService.get_connector_by_id(connector_id)
    if connector:
        return ConnectorResponse(**connector.get_dict())
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Connector Not Found"
    )


@router.put(
    "/{connector_id}",
    response_model=ConnectorResponse,
)
def update_connector(
    connector_id: conint(ge=1) = Path(..., alias="connectorId"),
    body: Connector = ...,  # noqa
) -> ConnectorResponse:
    """
    Update a Connector.
    """
    pass


@router.delete(
    "/{connector_id}",
    response_model=None,
)
def delete_connector(
    connector_id: conint(ge=1) = Path(..., alias="connectorId")
) -> None:
    """
    Remove a Connector.
    """
    pass
