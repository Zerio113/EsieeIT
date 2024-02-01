from .. import interface
from ..combat_entity.data import DATA as COMBAT_ENTITY_DATA
from .data import DATA

def _print_line(player, value_name):

    interface.print_(
        DATA["stats_view_line"].format(
            name=value_name.capitalize(),
            value=getattr(player.entity, value_name)
        )
    )

def stats_view(player):
    for value_name in COMBAT_ENTITY_DATA["entity_values"]:
        _print_line(player, value_name)

    interface.print_()

    for stat_name in COMBAT_ENTITY_DATA["stats"]:
        _print_line(player, stat_name)