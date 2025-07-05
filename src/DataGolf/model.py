from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

metadata = MetaData()

player_table = Table(
    'player', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('country', String, nullable=False),
    Column('country_code', String, nullable=False),
)

player_skills_table = Table(
    'player_skill', metadata,
    Column('player_id', Integer, primary_key=True),
    Column('sg_putting', Integer, nullable=False),
    Column('sg_approach', Integer, nullable=False),
    Column('sg_ott', Integer, nullable=False),
    Column('sg_arg', Integer, nullable=False),
    Column('sg_total', Integer, nullable=False),
    Column('driving_acc', Integer, nullable=False),
    Column('driving_dist', Integer, nullable=False),
)
