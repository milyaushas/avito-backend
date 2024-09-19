from src.db_models import Base
from src.contracts import Tender
from fastapi import Depends
import src.db_models as db_models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TenderManagerService:

    def __init__(self, postgres_url):
        self.engine = create_engine(postgres_url)
        self.SessionLocal = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        Base.metadata.create_all(bind=self.engine)

    def __get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_tenders(self):
        db = self.SessionLocal()
        return db.query(db_models.Tender).all()

    def create_tender(self, tender: Tender):
        if not tender:
            return None
        db = self.SessionLocal()

        creator_id = db.query(db_models.Employee).filter(db_models.Employee.username==tender.creatorUsername).first()

        if not creator_id:
            return None

        new_tender = db_models.Tender(
            name=tender.name,
            description=tender.description,
            service_type=tender.serviceType,
            status=tender.status,
            organization_id=tender.organizationId,
            creator_id=creator_id
        )
        db.commit()
        db.refresh(new_tender)
        tender['id'] = new_tender['id']
        return tender

    def get_tender_by_user_id(self, user_id):
        pass

    def update_tender(self, tender_id):
        pass

    def rollback_tender_to_version(self, tender_id, version):
        pass
