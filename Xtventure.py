import time
import sys
import random


def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def select_class():
    classes = {
        "Warrior": "⚔️ A battle-hardened soul, destined to carve a path through steel and blood.",
        "Archer": "🏹 A keen eye and a steady hand—your enemies will fall before they even see you.",
        "Assassin": "🗡️ Shadows will be your ally, and death will be your weapon.",
        "Mage": "🔮 The elements bend to your will. Magic is a gift… or a curse.",
        "Paladin": "🛡️ Light and steel intertwine. Will you bring salvation or judgment?",
        "Necromancer": "💀 Death does not end your power… it only begins it."
    }

    while True:
        type_text("Choose your path, reincarnated soul:")
        for class_name, description in classes.items():
            print(f" - {class_name}: {description}")

        my_class = input("Enter your class: ").strip().capitalize()

        if my_class in classes:
            confirm = input(f"You have chosen {my_class}. Confirm? (YES / NO): ").strip().lower()
            if confirm == "yes":
                type_text(f"Your destiny is set as a {my_class}... Eldoria awaits.")
                return my_class.lower()
            else:
                type_text("Re-selecting class...")
        else:
            type_text("Invalid choice. Please choose a valid class.")


def combat_sequence(player_class):
    """Handles the turn-based combat system."""
    enemy_hp = 25
    player_hp = 50
    class_attacks = {
        "warrior": {"Slash": (5, 8), "Rift Breaker": (7, 12)},
        "archer": {"Frost Shot": (6, 9), "Phantom Arrow": (7, 14)},
        "assassin": {"Ghoststep Slash": (9, 13), "Shadow Strike": (6, 10)},
        "mage": {"Fireball": (6, 9), "Soulburn": (8, 14)},
        "paladin": {"Holy Smite": (5, 8), "Divine Charge": (6, 9)},
        "necromancer": {"Dark Grasp": (8, 11), "Soul Drain": (8, 15)}
    }

    enemy_name = "The Forsaken Hound"
    type_text(f"A cursed beast, {enemy_name}, lunges at you from the shadows!")

    while enemy_hp > 0 and player_hp > 0:
        type_text("Choose your attack:")
        attacks = class_attacks.get(player_class.lower(), {"Basic Attack": (4, 6)})

        for attack in attacks:
            type_text(f" - {attack}")

        chosen_attack = input("Enter your attack: ").strip().title()

        if chosen_attack in attacks:
            damage = random.randint(*attacks[chosen_attack])
            enemy_hp -= damage
            type_text(f"You use {chosen_attack} and deal {damage} damage! {enemy_name} has {max(0, enemy_hp)} HP left!")
        else:
            type_text("Invalid attack! You miss your turn.")

        if enemy_hp <= 0:
            break

        time.sleep(1)
        type_text(f"{enemy_name} retaliates!")
        enemy_damage = random.randint(3, 7)
        player_hp -= enemy_damage
        type_text(f"You take {enemy_damage} damage. You have {max(0, player_hp)} HP left!")

        if player_hp <= 0:
            return seeker_rescue(defeated=True)  # Call the Seeker when the player collapses

    return seeker_rescue(defeated=False)  # Call the Seeker when the player wins


def seeker_rescue(defeated):   # Handles the Seeker's intervention based on the player's outcome.
    time.sleep(1)
    type_text("\nA figure in Dark Robes steps forward...")
    time.sleep(1)

    if defeated:
        type_text("The Seeker raises a hand, and a dark energy blade forms in the air.")
        type_text("With a single sweeping motion, the Forsaken Hound is cut in half.")
        type_text('"You are not ready for your fate yet," the Seeker says coldly.')
        type_text('"Train harder. Next time, no one will save you."')
        return False  # Player failed but gets to continue their journey

    else:
        type_text("As you catch your breath, you hear distant howls.")
        type_text("More Forsaken Hounds emerge from the mist, eyes glowing with hunger.")
        type_text("You are surrounded, outnumbered. There is no escape.")
        time.sleep(1)
        type_text("Just as the beasts close in, the Seeker appears in a blur of motion.")
        type_text("A wave of energy erupts from his blade, **disintegrating** the pack instantly.")
        type_text('"You are not ready for your fate yet," the Seeker says, turning away.')
        type_text('"Train harder. Next time, no one will save you."')


def chapter_one(player_class):
    type_text("You awaken in the ruins of a once-grand capital. The air is thick with a dark energy.")
    type_text("The wind howls through the broken streets, carrying whispers of the past.")

    type_text("As you rise to your feet, a hooded figure steps forward from the mist—silent, watchful.")

    type_text("???: 'Strange... it has been long since I’ve seen a living soul here.'")
    type_text("???: 'And yet, you do not carry the mark of the cursed. How did you arrive in this forsaken place?'")

    choice = input(
        "(1) 'I don’t know... I just woke up here.'\n(2) 'Who are you? What is this place?'\n").strip().lower()

    if choice == "1":
        type_text("You clutch your head, fragments of past and present colliding in confusion.")
        type_text(f"{name}: 'I... I don’t know. One moment, there was darkness... then, I was here.'")
    else:
        type_text(f"{name}: 'Before I answer, tell me who you are first. And where exactly is here?'")

    type_text("The figure studies you for a long moment, as if weighing the truth in your words.")

    type_text("???: 'Hmph. Questions before answers. You may yet survive here.'")
    type_text("???: 'I am called the Seeker. If you seek truth, I am all that remains to guide you.'")

    type_text(
        "The Seeker lifts his hood slightly, revealing piercing eyes—ancient, weary, yet burning with something unspoken.")

    time.sleep(0.5)
    type_text("Seeker: 'This city... was once the heart of Eldoria.'")
    type_text("Seeker: 'Now, it is a graveyard. A prison of despair where the dead do not rest.'")

    type_text(
        "The ruins seem to groan under some unseen weight, as if the city itself remembers the sorrow of its fall.")

    type_text("Seeker: 'Tell me, outsider... do you even recall your own name? Your purpose?'")

    choice = input(
        "(1) 'I remember my name... but nothing else.'\n(2) 'I remember... betrayal. And death.'\n").strip().lower()

    if choice == "1":
        type_text(f"{name}: 'I remember my name. But everything else is... fragments. Shadows in my mind.'")
        type_text("Seeker: 'Then you are no different from the rest. Lost, wandering, seeking purpose.'")
    else:
        type_text(f"{name}: 'I remember pain. A blade in my back. And then... nothing.'")
        type_text("The Seeker stiffens slightly, his expression unreadable.")
        type_text("Seeker: 'A soul torn from death’s embrace... I see now. You are no ordinary traveler.'")

    time.sleep(0.5)
    type_text("Seeker: 'The Dark Prophecy spoke of one who would either save or shatter this world.'")
    type_text("Seeker: 'I did not expect them to arrive in such... uncertain form.'")

    type_text("His gaze sharpens. Whatever hesitation he had, it is gone now.")

    choice = input(
        "(1) 'What is this prophecy?'\n(2) 'I don’t care about prophecy. I just want answers.'\n").strip().lower()

    if choice == "1":
        type_text("Seeker: 'The details are lost to time, but its weight remains.'")
        type_text("Seeker: 'A hero... or a destroyer. A soul reborn to shape Eldoria’s fate.'")
        type_text("Seeker: 'The question is, which will you become?'")
    else:
        type_text(f"{name}: 'Prophecy or not, I don’t care. I just want to know why I’m here.'")
        type_text("The Seeker narrows his eyes, as if measuring your resolve.")
        type_text("Seeker: 'Perhaps that is for you to discover. Or perhaps fate will force your hand.'")

    time.sleep(1)
    type_text("The distant sound of claws scraping against stone breaks the moment.")

    type_text("Seeker: 'Hmph. We are not alone.'")
    type_text("Seeker: 'The beast that approaches was once a noble guardian. Now, it is nothing but a Forsaken Hound.'")

    type_text(
        "Seeker: 'If you wish to learn the truth of this world, then fight. Prove your worth, or perish like the others who failed.'")

    success = combat_sequence(player_class)

    if success:
        type_text("Seeker watches you in silence as the beast falls.")
        type_text("Seeker: 'Impressive. You may yet have the strength to challenge fate.'")
        type_text("Seeker: 'But strength alone is not enough. Something far worse stirs beneath these ruins.'")
    else:
        type_text("The Seeker steps forward as you collapse, a dark energy forming at his fingertips.")
        type_text("With a swift motion, the Forsaken Hound is torn apart by unseen force.")
        type_text("Seeker: 'Pathetic. You will not survive long like this.'")
        type_text("Seeker: 'If you truly wish to shape your fate... then become stronger. Or die forgotten.'")

    time.sleep(1)
    type_text("Before you can respond, the Seeker fades into the mist, as if he were never there.")
    type_text("The journey has only begun...")
    return success

# Main Game Flow
print("Welcome to Xtventure.")
name = input("Enter Your Name: ")

type_text(
    "??? : Eldoria awaits you, child of fate. But beware... the prophecy speaks of one who shall either save or shatter the realm.")
type_text(f"{name}: Huh?! Where am I? Who’s there? What are you talking about?")

time.sleep(0.5)
type_text("??? : There isn’t much time. You must decide—what will you become in the wake of the Dark Prophecy?")

time.sleep(1)
type_text(f"{name}: What prophecy? Who are you? Show yourself!")

time.sleep(0.5)
type_text("??? : Names have power. You are not yet ready to know mine.")

type_text("The voice seems to echo from nowhere, yet everywhere. It carries a weight beyond mere words, as if pressing against your very soul.")

time.sleep(1)
type_text(f"{name}: This doesn’t make any sense! One moment I was... I was—")

time.sleep(0.5)
type_text("??? : You were betrayed. And you died.")

time.sleep(1)
type_text(f"{name}: ...")

type_text("The memories crash over you. A friend’s face twisted in treachery. The searing pain. The cold darkness that followed.")

time.sleep(1.5)
type_text(f"{name}: Then... why am I here?")

time.sleep(0.5)
type_text("??? : Because your story is not yet over. A greater force has woven your fate into Eldoria’s—")

time.sleep(0.5)
type_text("A deep rumble shakes the void around you. The voice hesitates, as if sensing something unseen.")

time.sleep(1)
type_text("??? : No. This is too soon. You must awaken.")

type_text(f"{name}: Wait! I don’t understand—!")

time.sleep(0.5)
type_text("??? : In time, you will. Seek the Seeker. He will show you the path… if you survive long enough to walk it.")

time.sleep(1)
type_text("A blinding light engulfs you. The voice fades. And then—")

type_text("—you wake up.")

decision = input(
    "\n(1) Quit this path and fade into oblivion.\n(2) Reincarnate into Eldoria and face your fate.\n").lower()

if decision in ("quit", "1"):
    type_text("And so, fate remains unchanged... Eldoria falls into ruin.")
elif decision in ("reincarnate into eldoria and face your fate", "2"):
    type_text("There is still hope... [REINCARNATING TO ELDORIA]")
    player_class = select_class()
    chapter_one(player_class)
else:
    type_text("Invalid choice. Destiny waits for no one...")




