
from sqlalchemy import create_engine, Column, String, DateTime, Enum, DECIMAL, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import datetime
import enum

# رابط الاتصال بقاعدة بيانات PostgreSQL على Render
DATABASE_URL = "postgresql://optitreasury_db_user:3TX4fyuNaApfFIw81wwsbFtyK4cOBVMU@dpg-d0jp51odl3ps73co7490-a.frankfurt-postgres.render.com/optitreasury_db"

# إعداد الاتصال
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# تعريف الصلاحيات
class RoleEnum(str, enum.Enum):
    admin = "admin"
    analyst = "analyst"
    viewer = "viewer"

# حالات المدفوعات
class StatusEnum(str, enum.Enum):
    draft = "draft"
    approved = "approved"
    rejected = "rejected"
    paid = "paid"

# جدول المستخدمين
class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_code = Column(String(20), nullable=False)
    full_name = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# جدول المدفوعات
class Payment(Base):
    __tablename__ = "payments"
    payment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_code = Column(String(20))
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    payment_date = Column(DateTime, nullable=False)
    amount = Column(DECIMAL(18, 2), nullable=False)
    currency = Column(String(10), default="SAR")
    beneficiary_name = Column(String(100))
    description = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.draft)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# تنفيذ إنشاء الجداول
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")
def get_db_connection():
    return engine.connect()

