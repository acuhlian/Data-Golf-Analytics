
def normalize_stat_category(normalized_data, stat_type, player, cat, full_cat):
    """Takes in string representing the stat type and
        adds that stat to its specific stat dict within
        data dict.
        e.g. 50_100_fw_gir_rate: value -> 50_100_fw : { gir_rate  : value}."""
    if full_cat not in normalized_data:
        normalized_data[full_cat] = {}
    normalized_data[full_cat][stat_type] = player[cat]