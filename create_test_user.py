from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import hashlib

# إعداد الاتصال بقاعدة البيانات (استبدلها إذا تغيرت)
DATABASE_URL = "postgresql://optitreasury_db_user:3TX4fyuNaApfFIw81wwsbFtyK4cOBVMU@dpg-d0jp51odl3ps73co7490-a.frankfurt-postgres.render.com/optitreasury_db"

# إعداد الجداول
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

# الاتصال وإنشاء الجلسة
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# إنشاء مستخدم تجريبي
test_email = "admin@opti.com"
test_password = "123456"

hashed_password = hashlib.sha256(test_password.encode()).hexdigest()

existing_user = session.query(User).filter_by(email=test_email).first()
if not existing_user:
    new_user = User(email=test_email, password=hashed_password)
    session.add(new_user)
    session.commit()
    print("تم إنشاء المستخدم بنجاح")
else:
    print("المستخدم موجود مسبقاً")

session.close()
