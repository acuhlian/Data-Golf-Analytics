import fetch
from sqlalchemy import insert, select
from model import engine, player_table, player_skills_table


def fill_player_list():
    player_list = fetch.fetch_player_list()
    with engine.connect() as conn:
        for player in player_list:
            insert_values = {
                'id': player['dg_id'],
                'name': player['player_name'],
                'country': player['country'],
                'country_code': player['country_code'],
            }
            stmt = insert(player_table).values(**insert_values)
            conn.execute(stmt)
            conn.commit()

def fill_player_skill_ratings():
    player_skill_list = fetch.fetch_player_skill_ratings()
    with engine.connect() as conn:
        for player in player_skill_list:
            insert_values = {
                'player_id' : player['dg_id'],
                'sg_putting': player['sg_putt'], 
                'sg_approach': player['sg_app'],
                'sg_ott' : player['sg_ott'],
                'sg_arg' : player['sg_arg'],
                'sg_total' : player['sg_total'],
                'driving_acc' : player['driving_acc'],
                'driving_dist' : player['driving_dist'],
            }
            result = conn.execute(select(player_table.c.id).where(player_table.c.id == player['dg_id'])).first()
            if result:
                stmt = insert(player_skills_table).values(**insert_values)
                conn.execute(stmt)
                conn.commit()
            else:
                print(f"Skipping skill for missing player_id={player['dg_id']}")
    return

if __name__ == "__main__":
    fill_player_skill_ratings()