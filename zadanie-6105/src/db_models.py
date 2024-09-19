from sqlalchemy import Column, String, TIMESTAMP, func, Text, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ENUM
import uuid
from sqlalchemy.orm import relationship
from src.contracts import OrganizationType, TenderStatus

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    type = Column(ENUM(OrganizationType))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    responsibilities = relationship("OrganizationResponsible", back_populates="organization")


class OrganizationResponsible(Base):
    __tablename__ = 'organization_responsible'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey('organization.id', ondelete='CASCADE'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('employee.id', ondelete='CASCADE'))


class Tender(Base):
    __tablename__ = 'tender'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    service_type = Column(String(100), nullable=True)
    status = Column(ENUM(TenderStatus), nullable=False)

    organization_id = Column(UUID(as_uuid=True), ForeignKey('organization.id'), nullable=False)
    creator_id = Column(UUID(as_uuid=True), ForeignKey('employee.id'), nullable=False)

    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    organization = relationship("Organization")
    creator = relationship("Employee")


class TenderVersion(Base):
    __tablename__ = 'tender_version'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tender_id = Column(UUID(as_uuid=True), ForeignKey('tender.id', ondelete='CASCADE'), nullable=False)

    version = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    service_type = Column(String(100), nullable=True)
    status = Column(ENUM(TenderStatus), nullable=False)
    organization_id = Column(UUID(as_uuid=True), ForeignKey('organization.id'), nullable=False)
    creator_id = Column(UUID(as_uuid=True), ForeignKey('employee.id'), nullable=False)

    tender = relationship("Tender")
