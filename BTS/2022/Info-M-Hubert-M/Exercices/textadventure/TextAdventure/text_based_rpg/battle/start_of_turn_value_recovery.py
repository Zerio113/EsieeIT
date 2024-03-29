from .. import interface
from .data import DATA

def start_of_turn_value_recovery(battle, entity):
    prior_stamina = entity.stamina
    prior_mana = entity.mana

    entity.restore_stamina_and_mana()

    stamina_restored = entity.stamina - prior_stamina
    mana_restored = entity.mana - prior_mana

    entity_name = battle.get_entity_name(entity)

    if stamina_restored:
        interface.print_(
            DATA["messages"][entity_name][
                "start_of_each_turn_stamina_regeneration"
            ].format(stamina_restored)
        )

    if mana_restored:
        interface.print_(
            DATA["messages"][entity_name][
                "start_of_each_turn_mana_regeneration"
            ].format(mana_restored)
        )
