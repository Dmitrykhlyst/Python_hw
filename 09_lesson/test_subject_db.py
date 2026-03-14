from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import pytest

# Модель Subject для таблицы subject
Base = declarative_base()

class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(255), nullable=False)

# Строка подключения к БД
db_connection_string = "postgresql://postgres:321@localhost/QA"
engine = create_engine(db_connection_string)

@pytest.fixture
def db_session():
    # Создаём таблицы перед тестом
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # передаём сессию в тест



def test_add_subject_to_db(db_session: Session):
    # Arrange: готовим тестовые данные для нового предмета
    test_title = "Математика"

    # Act: добавляем предмет в БД
    new_subject = Subject(subject_title=test_title)
    db_session.add(new_subject)

    try:
        db_session.commit()  # фиксируем транзакцию
    except Exception as e:
        pytest.fail(f"Ошибка при сохранении предмета в БД: {e}")

def test_update_subject_in_db(db_session: Session):
    # Arrange: создаём исходный предмет в БД
    original_title = "Математика"
    updated_title = "Высшая математика"

    # Добавляем исходный предмет
    subject = Subject(subject_title=original_title)
    db_session.add(subject)

    try:
        db_session.commit()  # фиксируем создание
    except Exception as e:
        pytest.fail(f"Ошибка при сохранении исходного предмета: {e}")

    assert subject.subject_id is not None, "subject_id не был сгенерирован при создании"

def test_delete_subject_with_query(db_session: Session):

    title1 = "Высшая математика"


    subject1 = Subject(subject_title=title1)
    db_session.add_all([subject1])
    db_session.commit()

    assert subject1.subject_id is not None


    # Act: используем явный запрос DELETE для первого предмета
    result = (
        db_session.query(Subject)
        .filter_by(subject_id=subject1.subject_id)
        .delete()
    )
    db_session.commit()



