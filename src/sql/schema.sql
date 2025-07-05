CREATE TABLE IF NOT EXISTS player(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    country_code TEXT NOT NULL
);

DROP TABLE player_skill;
CREATE TABLE player_skill (
    player_id INTEGER,
    sg_putting FLOAT NOT NULL,
    sg_approach FLOAT NOT NULL,
    sg_arg FLOAT NOT NULL,
    sg_ott FLOAT NOT NULL,
    sg_total FLOAT NOT NULL,
    driving_acc FLOAT NOT NULL,
    driving_dist FLOAT NOT NULL,
    FOREIGN KEY(player_id) REFERENCES player(id)
);
