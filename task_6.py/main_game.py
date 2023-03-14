"""
Main module for the game itself.
"""
import mygame

main_character = mygame.Character(
    "Pan Roman", "A devoted believer and has faith in Christ."
)

kozelnytska = mygame.Street("Kozelnytska street")
kozelnytska.set_description("A well-known street among UCU students.")

stryiska = mygame.Street("Stryiska street")
stryiska.set_description("")

franka = mygame.Street("Franka street")
franka.set_description(
    "A cozy street with numerous boutiques...\
 You must have expected to see a lot of cavaliers here, but only sleep-deprived students are here!"
)

krakivska = mygame.Street("Krakivska street")
krakivska.set_description("")

svobody = mygame.Street("Svobody avenue")
svobody.set_description("")

virmenska = mygame.Street("Virmens'ka street")
virmenska.set_description(
    "Oh, what a marvelous and cozy yard! Such a great place for those restaurants."
)

rohatyntsiv = mygame.Street("Brativ Rohatyntsiv street")
rohatyntsiv.set_description(
    "A very dangerous street, you may be encountered by Batyars!"
)

serbska = mygame.Street("Serbska street")
serbska.set_description(
    "A charming street in the heart of Lviv with Monument to Leopold von Sacher-Masoch and Lviv chocolate workshop."
)

kozelnytska.link_street(stryiska)
stryiska.link_street(franka)
stryiska.link_street(kozelnytska)

franka.link_street(svobody)
franka.link_street(stryiska)

svobody.link_street(virmenska)
svobody.link_street(franka)

virmenska.link_street(krakivska)
virmenska.link_street(svobody)

krakivska.link_street(rohatyntsiv)
krakivska.link_street(virmenska)

rohatyntsiv.link_street(serbska)
rohatyntsiv.link_street(krakivska)

serbska.link_street(rohatyntsiv)

drunken_cherry = mygame.Item("Piana Vyshnia")
drunken_cherry.set_description("A bottle of delicious famous liqueur.")
rohatyntsiv.set_item(drunken_cherry)

chocolate = mygame.Item("Chocolate")
chocolate.set_description("A bar of chocolate made by well-known workshop in Lviv.")
franka.set_item(chocolate)

crunchy_treat = mygame.Item("Crunchy treat")
crunchy_treat.set_description("Some crunchy treats for Levchyk.")
stryiska.set_item(crunchy_treat)

cheese_balls = mygame.Item("Cheese balls")
cheese_balls.set_description("A packet of cheese balls for Levchyk.")

chicken_treat = mygame.Item("Chicken treat")
chicken_treat.set_description(
    "A mouth-watering chicken treat, that every cat would sell their soul to eat."
)

tasty_vitamins = mygame.Item("Tasty vitamins")
tasty_vitamins.set_description(
    "Some delicious vitamins for Levchyk to be healthy and satisfied."
)
krakivska.set_item(tasty_vitamins)

coffee = mygame.Item("Coffee")
coffee.set_description("A drink for every person, who couldn't sleep.")
kozelnytska.set_item(coffee)

sadovyi = mygame.Friend("Andriy Sadovyi", "A dedicated mayor to his city and citizens.")
sadovyi.set_conversation(
    "Greetings, my friend! I have a huge problem that I cannot fix myself.\
 Levchyk is so miserable these days, I bet he misses his favourite snacks.\
 As I'm taking care of the well-being of the city, I simply cannot deal with this problem now.\
 Could you find some snack for Levchyk to make him feel better? "
)
kozelnytska.set_character(sadovyi)

batyar = mygame.Batyar()
batyar.set_wanted_item("Piana Vyshnia")
rohatyntsiv.set_character(batyar)

lotr = mygame.Lotr()
lotr.set_wanted_item("Chocolate")
svobody.set_character(lotr)

student = mygame.Student()
student.set_wanted_item("Coffee")
student.torba.append(chicken_treat)
franka.set_character(student)

cat_levchyk = mygame.Levchyk(
    [crunchy_treat, cheese_balls, tasty_vitamins, chicken_treat]
)
serbska.set_character(cat_levchyk)

cavalier = mygame.Cavalier()
cavalier.torba.append(cheese_balls)
virmenska.set_character(cavalier)

current_street = kozelnytska
FAILED = False

while FAILED is False:
    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    if isinstance(inhabitant, mygame.Levchyk):
        if inhabitant.check_treats(main_character.torba):
            print(
                "Congratulations, you succeded and found all the desired treats for Levchyk,\
 now his cat life will be even more fulfilling!"
            )
        else:
            FAILED = True
            break

    command = input("> ")

    if command in current_street.get_destinations():
        # Move in the given direction
        next_street = current_street.move(command)

        if inhabitant is not None and isinstance(inhabitant, mygame.Enemy):
            print(f"You encountered an enemy - {inhabitant.name}!")

            inhabitant.demand(main_character)
            print(f"Will you accept {inhabitant.name} demands? (Y/N)")
            should_proceed = input("> ")

            if should_proceed == "Y" and main_character.give(inhabitant.wanted_item):
                print(
                    f"{inhabitant.name} is happy with {inhabitant.wanted_item}! You can proceed!"
                )
            else:
                print(
                    f"You do not have what {inhabitant.name} wants. You cannot go further!"
                )
                FAILED = True

        if inhabitant is not None and isinstance(inhabitant, mygame.Friend):
            inhabitant.notify_of_danger(next_street)
            should_proceed = input("Do you want to proceed? (Y/N) > ")

            if should_proceed == "Y":
                current_street = next_street
            else:
                print("You decided to stay on " + current_street.name)

            if (
                isinstance(inhabitant, mygame.Cavalier)
                and len(inhabitant.torba) != 0
                and inhabitant.give(inhabitant.torba[0].name)
            ):
                main_character.torba.append(inhabitant.torba[0])

            if isinstance(inhabitant, mygame.Student):
                print(
                    f"You encountered - {inhabitant.name}! He wants {inhabitant.wanted_item}.\
 Can you give it to him? (Y/N)"
                )
                should_proceed = input("> ")

                if (
                    should_proceed == "Y"
                    and main_character.give(inhabitant.wanted_item)
                    and inhabitant.give(inhabitant.torba[0].name)
                ):
                    print(
                        f"{inhabitant.name} is happy with {inhabitant.wanted_item}!\
 You can proceed!"
                    )
                    main_character.torba.append(inhabitant.torba[0])

        else:
            current_street = next_street
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "take":
        if item is not None:
            print(item.get_name() + " was added to your torba.")
            main_character.torba.append(item)
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")

    else:
        print("I don't know how to " + command)
