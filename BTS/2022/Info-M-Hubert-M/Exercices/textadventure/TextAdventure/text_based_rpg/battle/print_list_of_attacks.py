from .. import interface
from .data import DATA

def print_list_of_attacks(battle):
    for attack in battle.player.entity.attacks:
        line = attack.display_name + " --- Dommage: " + str(attack.damage) + ". "

        if attack.stamina_cost:
            line += DATA["list_of_attacks"]["stamina_cost_template"].format(
                attack.stamina_cost
            )

        if attack.mana_cost:
            line += DATA["list_of_attacks"]["mana_cost_template"].format(
                attack.mana_cost
            )

        interface.print_(line)
