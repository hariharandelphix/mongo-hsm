#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import Dict, List, Optional

from pydantic import BaseModel, Field, constr
from src.validators.executions_validator import ExecutionStatus, Status


class ObjectDetail(BaseModel):
    type: Optional[str] = Field(
        None, description="Component type of Post Load Task Component Status."
    )
    total: Optional[int] = Field(
        None, description="Total components of all Post Load Task Components."
    )
    processed: Optional[int] = Field(
        None,
        description="Processed components of all Post Load Task Components.",  # noqa
    )
    status: Optional[Status] = Field(
        None, description="The status of the load process."
    )
    start_time: Optional[str] = Field(
        None, description="The time when the load process is started."
    )
    end_time: Optional[str] = Field(
        None,
        description="The time when the post load task component process is completed.",  # noqa
    )
    error: Optional[str] = Field(None, description="Error details.")


class DataInfoItem1(BaseModel):
    source_key: Dict[str, str] = Field(
        ...,
        description="object providing the information like schema_name, table_name or file_name of the source datasource",  # noqa
    )
    rows_loaded: Optional[int] = Field(
        None, description="Total number of rows loaded to the database table."
    )
    masked_file_path: Optional[constr(min_length=1)] = Field(
        None, description="relative path of the target masked file."
    )
    status: Optional[Status] = Field(
        None, description="The status of the load process."
    )
    error: Optional[str] = Field(None, description="Error details.")


class DataInfoItem2(BaseModel):
    table_set: Optional[List[str]] = Field(
        None,
        description="Array of multiple table set for post load task.",
        max_items=10000,
        min_items=1,
    )
    object_details: Optional[List[ObjectDetail]] = Field(
        None,
        description="Array of multiple post load task object details, each component providing the information like total and processed.",  # noqa
        max_items=10000,
        min_items=1,
    )


class LoadResponse(ExecutionStatus):
    execution_id: int = Field(..., description="ID of the Execution model.")
    job_id: int = Field(..., description="ID of the registered Job model.")
    start_time: Optional[str] = Field(
        None, description="The time when the load process is started."
    )
    end_time: Optional[str] = Field(
        None, description="The time when the load process is completed."
    )
    data_info: Optional[List[DataInfoItem1]] = Field(
        None,
        description="Array of multiple objects, each object providing the information like sourceKey and file_info.",  # noqa
        max_items=10000,
        min_items=1,
    )


class PostLoadResponse(BaseModel):
    id: Optional[int] = None
    execution_id: Optional[int] = Field(
        None, description="Post Load Response model."
    )  # noqa
    status: Status = Field(
        ..., description="The status of the post load process."
    )  # noqa
    start_time: str = Field(
        ..., description="The time when the load process is started."
    )
    end_time: Optional[str] = Field(
        None,
        description="The time when the post load task component process is completed.",  # noqa
    )
    data_info: Optional[List[DataInfoItem2]] = Field(
        None,
        description="Array of multiple table set with corresponding task object details for post load task.",  # noqa
        max_items=10000,
        min_items=1,
    )
    error: Optional[str] = Field(None, description="Error details.")
