import random
from time import sleep as s


def hunt(aggressor, defender):

    #first part is camouflage check
    if random.randint(1,100) > 50 * (defender.hiding_power / aggressor.sight_power):
    #if creature has access to a sneak attack move it will go here, and it will override the second check if successful
    #second check is a speed check
        if aggressor.speed >= defender.speed:
    #third is the fight


            aggressor_hp = aggressor.size * 2
            defender_hp = defender.size * 2

            attacks = {
                # sharp attack blunt attack piercing attack modifiers
                "bite": [1.5, 0, .5]
            }

            # for the most part this is a placeholder
            # base amount is one and for damage reduction will half damage 2 will do 75 percent off
            # example stats "damage reduction", "damage return", ""
            # posin and venom
            defender_counters = {
                "bite": [[defender.traits.defensive_spikes, {"overall damage reduction": 1, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 1,}]]
            }

            aggressor_counters = {
                "bite": [[aggressor.traits.defensive_spikes, {"overall damage reduction": 1, "sharp damage reduction": 0, "blunt damage reduction": 0, "piercing damage reduction": 0, "damage return": 1, }]]
            }


            while aggressor_hp > 0 and defender_hp > 0:
                aggressor_attack = aggressor.attack_moves[random.randint(0,len(aggressor.attack_moves)-1)]
                #if spikes = 100 half health of 15 size creature so 15 damage
                # abriviated words got to long
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
                damage = damage * random.randint(1,3) / 2

                defender_hp -= damage
                aggressor_hp -= damage_return_from_counter



                if defender_hp <= 0 or aggressor_hp <= 0:
                    break

                defender_attack = defender.attack_moves[random.randint(0, len(aggressor.attack_moves) - 1)]
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

                damage = ((aggressor.sharp_attacking_power * sdrfc * attacks[defender_attack][0]) + (defender.blunt_attacking_power * bdrfc * attacks[defender_attack][1]) + (aggressor.piercing_attacking_power * pdrfc * attacks[defender_attack][2])) * odrfc
                damage = damage * random.randint(1,3) / 2

                aggressor_hp -= damage
                defender_hp -= damage_return_from_counter



            if defender_hp <= 0:
                defender.die(defender.nutritinal_output-aggressor.nutritinal_need)
                return True
            elif aggressor_hp <= 0:
                if random.randint(1,10) == 1:
                    aggressor.die()
                return False

    return False
