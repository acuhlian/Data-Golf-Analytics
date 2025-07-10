CREATE TABLE IF NOT EXISTS player(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    country_code TEXT NOT NULL
);

DROP TABLE IF EXISTS player_skill;
CREATE TABLE IF NOT EXISTS player_skill (
    player_id INTEGER PRIMARY KEY,
    sg_putting FLOAT NOT NULL,
    sg_approach FLOAT NOT NULL,
    sg_arg FLOAT NOT NULL,
    sg_ott FLOAT NOT NULL,
    sg_total FLOAT NOT NULL,
    driving_acc FLOAT NOT NULL,
    driving_dist FLOAT NOT NULL,
    FOREIGN KEY(player_id) REFERENCES player(id)
);
/*Shot category is a normalized version of data golf's API
  Allows for easy modification of database if more specific categories
  are released
  AS OF 7/5/2025
  - Filter detailed skill data based on following shot categories
  1. 50_100_fw
  2. 100_150_fw
  3. 150_200_fw
  4. over_200_fw
  5. under_150_rgh
  6. over_150_rgh
 */
CREATE TABLE IF NOT EXiSTS player_skill_app (
    player_id INTEGER,
    shot_category TEXT,
    shot_count INTEGER,
    low_data_indicator INTEGER,
    sg_per_shot FLOAT,
    proximity_per_shot FLOAT,
    gir_rate FLOAT,
    good_shot_rate FLOAT,
    poor_shot_avoid_rate FLOAT,
    FOREIGN KEY(player_id) REFERENCES player(id), 
    CONSTRAINT player_skill_id UNIQUE (player_id, shot_category)
);
