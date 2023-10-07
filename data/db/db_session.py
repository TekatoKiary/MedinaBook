import sqlalchemy as sa
from sqlalchemy.engine.base import Engine
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory
    if __factory:
        return
    check_db_file_name(db_file)
    engine = get_engine(db_file)
    __factory = orm.sessionmaker(bind=engine)
    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def check_db_file_name(db_file):
    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")


def get_engine(db_file) -> Engine:
    connect_string = f"sqlite:///{db_file.strip()}?check_same_thread=False"
    print(f"Подключение к базе данных по адресу {connect_string}")
    return sa.create_engine(connect_string, echo=False)


def create_session() -> Session:
    global __factory
    return __factory()
