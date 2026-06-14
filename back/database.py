# 数据库连接代码
from sqlalcehmy import create_engine
from sqlalcehmy.orm import sessionmaker,declarative_base

# 建立数据库
SQLALCHEMY_URL="sqlite:///./notebook.db"

# 人话建立引擎
engine=create_engine(SQLALCEHMY_URL,connect_args={"check_same_thread":False})

sessionlocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()