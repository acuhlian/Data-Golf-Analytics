import fetch
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from model import (engine, player_table, player_skills_table,
                   player_skills_app_table)


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
            conflicts = ["id"]
                
            upsert_stmt = stmt.on_conflict_do_update(
                index_elements = conflicts,
                set_= {col: stmt.excluded[col] for col in insert_values.keys()}
            )
            conn.execute(upsert_stmt)
            conn.commit()
    print("Player list updated")

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
                conflicts = ["player_id"]
                
                upsert_stmt = stmt.on_conflict_do_update(
                    index_elements = conflicts,
                    set_= {col: stmt.excluded[col] for col in insert_values.keys()}
                )
                conn.execute(upsert_stmt)
                conn.commit()
            else:
                print(f"Skipping skill for missing player_id={player['dg_id']}")
    print("Player skill ratings updated")

def fill_player_skills_app():
    player_skill_app_list = fetch.fetch_player_skill_app()
    with engine.connect() as conn: 
        for player in player_skill_app_list:
            dg_id = player['dg_id']
            for cat in player:
                if cat in ['player_name', 'dg_id']:
                    continue
                insert_values = {
                    'player_id' : dg_id,
                    'shot_category' : cat,
                    'shot_count' : player[cat]['shot_count'],
                    'sg_per_shot' : player[cat]['sg_per_shot'],
                    'proximity_per_shot' : player[cat]['proximity_per_shot'],
                    'gir_rate' : player[cat]['gir_rate'],
                    'good_shot_rate' : player[cat]['good_shot_rate'],
                    'poor_shot_avoid_rate' : player[cat]['poor_shot_avoid_rate'],
                }
                result = conn.execute(select(player_table.c.id).where(player_table.c.id == dg_id)).first()
                if result:
                    stmt = insert(player_skills_app_table).values(**insert_values)
                    conflicts = ["player_id", "shot_category"]
                    conflict_stmt = stmt.on_conflict_do_update(
                        index_elements = conflicts,
                        set_={col: stmt.excluded[col] for col in insert_values.keys()}
                    )
                    conn.execute(conflict_stmt)
                    conn.commit()
                else:
                    print(f"Skipping skill for missing player_id={player['dg_id']}")
    print("Player skill approach updated")


if __name__ == "__main__":
    fill_player_list()
    fill_player_skills_app()
    fill_player_skill_ratings()