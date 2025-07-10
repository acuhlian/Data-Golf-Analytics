from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, TEXT, MetaData, ForeignKey, FLOAT)
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
    Column('player_id', Integer, ForeignKey('player.id', ondelete='CASCADE'), nullable=False),
    Column('sg_putting', FLOAT, nullable=False),
    Column('sg_approach', FLOAT, nullable=False),
    Column('sg_ott', FLOAT, nullable=False),
    Column('sg_arg', FLOAT, nullable=False),
    Column('sg_total', FLOAT, nullable=False),
    Column('driving_acc', FLOAT, nullable=False),
    Column('driving_dist', FLOAT, nullable=False),
)

player_skills_app_table = Table(
    'player_skill_app', metadata,
    Column('player_id', Integer, ForeignKey('player.id', ondelete='CASCADE'), primary_key=True),
    Column('shot_category', TEXT, nullable=False),
    Column('shot_count', Integer, nullable=False),
    Column('sg_per_shot', FLOAT, nullable=False),
    Column('proximity_per_shot', FLOAT, nullable=False),
    Column('gir_rate', FLOAT, nullable=False),
    Column('good_shot_rate', FLOAT, nullable=False),
    Column('poor_shot_avoid_rate', FLOAT, nullable=False),
)