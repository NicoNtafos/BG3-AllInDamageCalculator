import sys


def main():

    prompt_user()


def prompt_user():

    print("Do you want to perform a damage calculation or adjust your damage dice?")
    print("1. Damage Calculation")
    print("2. Adjust Damage Dice")
    print("3. Exit Program")

    operation = str(input())

    if operation != "1" and operation != "2" and operation != "3":
        raise Exception("Operation input invalid - select 1, 2, or 3")
    print("")

    if operation == "1":
        calculate_dmg()
    elif operation == "2":
        adjust_dice()
    else:
        sys.exit(0)

# Checks that accuracy input is valid, used in calculate_dmg()
def check_accuracy(accuracy):
    if accuracy < 1 or accuracy > 100:
        raise Exception("Accuracy input invalid - must be between 1 and 100")


# TODO - Implement below method
def calculate_kill_chance(min_dmg, max_dmg):
    return "WIP"


def calculate_dmg():
    print("What is your chance to hit with sharpshooter? (Enter w/o percent sign): ")
    ss_accuracy = int(input())
    check_accuracy(ss_accuracy)
    ss_accuracy /= 100

    print("What is your chance to hit without sharpshooter? (Enter w/o percent sign): ")
    base_accuracy = int(input())
    check_accuracy(base_accuracy)
    base_accuracy /= 100

    print("Without sharpshooter, what is the bottom of your damage range?")
    base_min_dmg = int(input())

    print("Without sharpshooter, what is the top of your damage range?")
    base_max_dmg = int(input())

    print("What is your target's HP?")
    target_hp = int(input())

    ss_min_dmg = base_min_dmg + 10
    ss_max_dmg = base_max_dmg + 10

    base_hit_dmg = (base_min_dmg + base_max_dmg) / 2
    ss_hit_dmg = (ss_min_dmg + ss_max_dmg) / 2

    base_expected_dmg = base_accuracy * base_hit_dmg
    ss_expected_dmg = ss_accuracy * ss_hit_dmg

    ss_dmg_diff = ss_expected_dmg - base_expected_dmg

    print("Expected damage change with sharpshooter: " + str(ss_dmg_diff))

    # TODO - Add calculation for kill chance given enemy HP
    # Tested above calculation and it works as expected

    print("")
    prompt_user()


# TODO - Finish implementing
def adjust_dice():
    print("WIP")
    print("")
    prompt_user()


if __name__ == "__main__":
    main()
