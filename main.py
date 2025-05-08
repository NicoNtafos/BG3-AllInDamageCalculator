import sys
import numpy as np
import re

def main():
    prompt_user()

def prompt_user():
    print("Press 1 to start a new damage calculation or 2 to quit")

    operation = str(input())

    if operation != "1" and operation != "2":
        raise Exception("Input invalid - select 1 or 2")
    print("")

    if operation == "1":
        calculate_dmg()
    else:
        sys.exit(0)

def calculate_dmg():
    print("What is your damage range with \"All In\" OFF?")
    base_damage_vals = re.findall(r'\d+', str(input()))
    base_min_dmg = int(base_damage_vals[0])
    base_max_dmg = int(base_damage_vals[1])

    print("What is your chance to hit with \"All In\" OFF? (Enter w/o percent sign): ")
    base_hit_chance = int(input())
    check_hit_chance(base_hit_chance)
    base_hit_chance /= 100

    print("What is your chance to hit with \"All In\" ON? (Enter w/o percent sign): ")
    ss_hit_chance = int(input())
    check_hit_chance(ss_hit_chance)
    ss_hit_chance /= 100

    print("What is your target's HP?")
    target_hp = int(input())

    ss_min_dmg = base_min_dmg + 10
    ss_max_dmg = base_max_dmg + 10

    base_hit_dmg = (base_min_dmg + base_max_dmg) / 2
    ss_hit_dmg = (ss_min_dmg + ss_max_dmg) / 2

    print("Average expected damage with \"All In\" ON: " + str(round(ss_hit_chance * ss_hit_dmg, 2)))
    print("Average expected damage with \"All In\" OFF: " + str(round(base_hit_chance * base_hit_dmg, 2)))

    # TODO - add unit tests - manually tested all calculations except kill chance and it works as expected
    print("Kill chance with \"All In\" ON: " + str(round(calculate_kill_chance(ss_min_dmg, ss_max_dmg, target_hp, ss_hit_chance), 2)) + "%")
    print("Kill chance with \"All In\" OFF: " + str(round(calculate_kill_chance(base_min_dmg, base_max_dmg, target_hp, base_hit_chance), 2)) + "%")

    print("")
    prompt_user()

# Checks that hit chance input is valid, used in calculate_dmg()
def check_hit_chance(hit_chance):
    if hit_chance < 1 or hit_chance > 100:
        raise Exception("Hit chance input invalid - must be between 1 and 100")

def calculate_kill_chance(min_dmg, max_dmg, hp, hit_chance):
    damage_values = np.arange(min_dmg, max_dmg + 1)
    total_damage_vals = damage_values.size

    kill_damage_vals = 0
    for val in damage_values:
        if val >= hp:
            kill_damage_vals += 1

    kill_chance_if_hit = kill_damage_vals / total_damage_vals
    return hit_chance * kill_chance_if_hit * 100

if __name__ == "__main__":
    main()
