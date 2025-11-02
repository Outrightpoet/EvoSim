import random
from random_store import get_randint_one_three, get_randint_one_ten


def hunt(aggressor, defender):

    #first part is camouflage check
    if random.randint(1,100) > 50 * (defender.hiding_power / aggressor.sight_power):
    #if creature has access to a sneak attack move it will go here, and it will override the second check if successful
    #second check is a speed check
        if aggressor.speed >= defender.speed or (aggressor.traits.camouflage + get_randint_one_ten()) >= (defender.traits.sight + get_randint_one_ten()) and (aggressor.traits.soft_feet + get_randint_one_ten()) >= (defender.traits.hearing + get_randint_one_ten()):
    #third is the fight


            aggressor_hp = (aggressor.size * 2) + (aggressor.traits.thick_skin / 4) + (aggressor.traits.dense_muscles / 8)
            defender_hp = (defender.size * 2) + (defender.traits.thick_skin / 4) + (aggressor.traits.dense_muscles / 8)

            attacks = {
                # sharp attack blunt attack piercing attack modifiers
                "bite": [1.5, 0, .5],
                "claw": [2.5, 0, 0],
                "tail whip": [1.5, 1, 0],
                "club": [0, 3, 0],
                "horn stab": [.5, 0, 3],
                "stomp": [.5, 1, .5]
            }

            # for the most part this is a placeholder
            # base amount is one and for damage reduction will half damage 2 will do 75 percent off
            # example stats "damage reduction", "damage return", ""
            # posin and venom
            #[defender.traits.defensive_spikes, {"overall damage reduction": 0, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
            defender_counters = {
                "bite": [[defender.traits.defensive_spikes, {"overall damage reduction": 1, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 1,}],
                         [defender.traits.thick_skin, {"overall damage reduction": 1, "sharp damage reduction": .5, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                         [defender.traits.bone_plates, {"overall damage reduction": 2, "sharp damage reduction": 2, "blunt damage reduction": 0, "piercing damage reduction": 1, "damage return": 0,}],
                         [defender.traits.scales, {"overall damage reduction": .5, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                         ],
                "claw": [[defender.traits.thick_skin, {"overall damage reduction": 1, "sharp damage reduction": .5, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                         [defender.traits.bone_plates, {"overall damage reduction": 2, "sharp damage reduction": 2, "blunt damage reduction": 0, "piercing damage reduction": 1, "damage return": 0,}],
                         [defender.traits.scales, {"overall damage reduction": .5, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                         ],
                "tail whip": [[defender.traits.defensive_spikes, {"overall damage reduction": .25, "sharp damage reduction": 1, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": .5,}],
                              [defender.traits.thick_skin, {"overall damage reduction": 1, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                              [defender.traits.bone_plates, {"overall damage reduction": 2, "sharp damage reduction": 2, "blunt damage reduction": 0, "piercing damage reduction": 1, "damage return": 0,}],
                              [defender.traits.scales, {"overall damage reduction": 1.5, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                              ],
                "club": [[defender.traits.defensive_spikes, {"overall damage reduction": .25, "sharp damage reduction": .5, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": .5,}],
                         [defender.traits.bone_plates, {"overall damage reduction": .5, "sharp damage reduction": 3.5, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                         [defender.traits.scales, {"overall damage reduction": .5, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                         ],
                "horn stab": [[defender.traits.defensive_spikes, {"overall damage reduction": .25, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                              [defender.traits.thick_skin, {"overall damage reduction": 0, "sharp damage reduction": 1, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                              [defender.traits.bone_plates, {"overall damage reduction": 1, "sharp damage reduction": 3, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                              [defender.traits.scales, {"overall damage reduction": .5, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": .5, "damage return": 0,}],
                              ],
                "stomp": [[defender.traits.defensive_spikes, {"overall damage reduction": .25, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": .5,}],
                          [defender.traits.thick_skin, {"overall damage reduction": 0, "sharp damage reduction": 1, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                          [defender.traits.bone_plates, {"overall damage reduction": 2, "sharp damage reduction": 2, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 0,}],
                          [defender.traits.scales, {"overall damage reduction": .5, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": .5, "damage return": 0,}],
                          ]
            }

            aggressor_counters = {
                "bite": [[aggressor.traits.defensive_spikes, {"overall damage reduction": 1, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 1, }]]
            }


            while aggressor_hp > 0 and defender_hp > 0:
                aggressor_attack = aggressor.attack_moves[random.randint(0,len(aggressor.attack_moves)-1)]
                #if spikes = 100 half health of 15 size creature so 15 damage
                # abriviated words got to long
                #overall damage reduction for creature
                odrfc = 1
                sdrfc = 1
                bdrfc = 1
                pdrfc = 1
                damage_return_from_counter = 0
                for counter in defender_counters[aggressor_attack]:
                    if counter[0] > 0:


                        odrfc = odrfc * (1-(counter[0]*(counter[1]["overall damage reduction"]/200)))
                        sdrfc = sdrfc * (1-(counter[0]*(counter[1]["sharp damage reduction"]/200)))
                        bdrfc = bdrfc * (1 - (counter[0] * (counter[1]["blunt damage reduction"] / 200)))
                        pdrfc = pdrfc * (1 - (counter[0] * (counter[1]["piercing damage reduction"] / 200)))
                        damage_return_from_counter += (counter[0] * .15) * counter[1]["damage return"]


                damage = ((aggressor.sharp_attacking_power * sdrfc * attacks[aggressor_attack][0]) + (defender.blunt_attacking_power * bdrfc * attacks[aggressor_attack][1]) + (aggressor.piercing_attacking_power * pdrfc * attacks[aggressor_attack][2])) * odrfc
                #adding some randomness to encounters
                damage = damage * get_randint_one_three() / 2

                defender_hp -= damage
                aggressor_hp -= damage_return_from_counter



                if defender_hp <= 0 or aggressor_hp <= 0:
                    break

                defender_attack = defender.attack_moves[random.randint(0, len(defender.attack_moves) - 1)]
                # if spikes = 100 half health of 15 size creature so 15 damage
                # abriviated words got to long
                odrfc = 1
                sdrfc = 1
                bdrfc = 1
                pdrfc = 1
                damage_return_from_counter = 0
                for counter in aggressor_counters[defender_attack]:
                    if counter[0] > 0:

                        odrfc = odrfc * (1 - (counter[0] * (counter[1]["overall damage reduction"] / 200)))
                        sdrfc = sdrfc * (1 - (counter[0] * (counter[1]["sharp damage reduction"] / 200)))
                        bdrfc = bdrfc * (1 - (counter[0] * (counter[1]["blunt damage reduction"] / 200)))
                        pdrfc = pdrfc * (1 - (counter[0] * (counter[1]["piercing damage reduction"] / 200)))
                        damage_return_from_counter += (counter[0] * .15) * counter[1]["damage return"]

                damage = ((defender.sharp_attacking_power * sdrfc * attacks[defender_attack][0]) + (defender.blunt_attacking_power * bdrfc * attacks[defender_attack][1]) + (defender.piercing_attacking_power * pdrfc * attacks[defender_attack][2])) * odrfc
                damage = damage * get_randint_one_three() / 2

                aggressor_hp -= damage
                defender_hp -= damage_return_from_counter



            if defender_hp <= 0:
                defender.die(defender.nutritinal_output-aggressor.nutritinal_need)
                return True
            elif aggressor_hp <= 0:
                if get_randint_one_ten() == 1:
                    aggressor.die()
                return False

    return False
