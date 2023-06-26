# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DataSetJobMapping(Base):
    __tablename__ = "data_set_job_mapping"

    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)


class Load(Base):
    __tablename__ = "load"

    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)


class PostLoad(Base):
    __tablename__ = "post_load"

    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)
