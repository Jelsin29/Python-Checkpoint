import random

def start_game():
    print("\nWelcome to 'The Asylum in the Woods'")
    print("You are Javier, a psychology student about to start your internship at a remote psychiatric hospital.")
    print("The autumn wind blows cold as dry leaves crunch beneath your feet. You've always been drawn to the paranormal,")
    print("and the eerie atmosphere only excites you more.")
    print("You and three other students - Lucy, Julián, and Román - are the unlucky ones assigned to this distant facility.")
    print("Rumors and urban legends surround this place, but you're determined to prove yourself.")
    return arrive_at_asylum()

def arrive_at_asylum():
    print("\nAfter a long journey, you arrive at the asylum. The building looks old and somewhat neglected from the outside,")
    print("its thick walls looming ominously against the darkening sky.")
    print("1. Enter the building")
    print("2. Hesitate and look around")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        return enter_asylum()
    elif choice == "2":
        return look_around()
    else:
        print("Invalid choice. Please try again.")
        return arrive_at_asylum()

def enter_asylum():
    print("\nYou step inside, and your jaw drops. The interior is surprisingly luxurious, a stark contrast to its exterior.")
    print("Polished floors, expensive furniture, and tasteful decorations adorn the space.")
    print("Director Paul Monroe, a tall man with a worn face and bushy eyebrows, greets you and your fellow interns.")
    print("His serious demeanor and prominent jawline remind you of a modern-day Frankenstein.")
    print("1. Listen to the director's instructions")
    print("2. Ask about the patients")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        return listen_to_director()
    elif choice == "2":
        return ask_about_patients()
    else:
        print("Invalid choice. Please try again.")
        return enter_asylum()

def look_around():
    print("\nAs you hesitate, you take in your surroundings. The asylum is encircled by a dense, foreboding forest.")
    print("A shiver runs down your spine, but you can't tell if it's from the cold or a sense of foreboding.")
    return enter_asylum()

def listen_to_director():
    print("\nDirector Monroe gives you a brief, cold overview of your duties.")
    print("As he shows you to your room, you notice how vast the facility is, with long corridors and numerous doors.")
    print("Suddenly, an overwhelming wave of fatigue washes over you. You decide to take a quick nap...")
    return wake_up_confused()

def ask_about_patients():
    print("\nDirector Monroe's face twitches almost imperceptibly. He gives a vague answer about various mental illnesses,")
    print("but you sense there's something he's not telling you.")
    print("As he leads you to your room, you're struck by an inexplicable, intense drowsiness...")
    return wake_up_confused()

def wake_up_confused():
    print("\nYou jolt awake, disoriented and groggy. To your shock, you realize many hours have passed.")
    print("Your mind feels foggy, and you struggle to piece together what happened.")
    print("1. Go find your fellow interns")
    print("2. Explore the asylum alone")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        return find_interns()
    elif choice == "2":
        return explore_alone()
    else:
        print("Invalid choice. Please try again.")
        return wake_up_confused()

def find_interns():
    print("\nYou find Lucy in the corridor. Her fiery red curls frame a face etched with worry.")
    print("She seems relieved to see you, but there's fear in her eyes.")
    print("1. Ask Lucy what's wrong")
    print("2. Suggest exploring the asylum together")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        return ask_lucy()
    elif choice == "2":
        return explore_with_lucy()
    else:
        print("Invalid choice. Please try again.")
        return find_interns()

def explore_alone():
    print("\nThe asylum seems different now - quieter, more ominous. As you walk the halls,")
    print("you hear strange noises coming from behind a locked door at the end of a dimly lit corridor.")
    print("1. Try to open the door")
    print("2. Go back to find others")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        return try_door()
    elif choice == "2":
        return find_interns()
    else:
        print("Invalid choice. Please try again.")
        return explore_alone()

def ask_lucy():
    print("\nLucy's voice trembles as she speaks. She tells you about strange occurrences in the asylum -")
    print("patients disappearing, odd noises at night, and staff acting suspiciously.")
    print("She's scared but determined to uncover the truth.")
    return explore_with_lucy()

def explore_with_lucy():
    print("\nAs you and Lucy cautiously explore the asylum, alarms suddenly start blaring.")
    print("Red emergency lights bathe the corridors in an eerie glow. Panic starts to set in.")
    print("1. Go to the director's office")
    print("2. Try to leave the asylum")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        return directors_office()
    elif choice == "2":
        return try_to_leave()
    else:
        print("Invalid choice. Please try again.")
        return explore_with_lucy()

def try_door():
    print("\nThe door is locked. As you turn to leave, you see a figure at the end of the hallway, staring at you.")
    print("Its eyes are vacant, almost white. Suddenly, it starts running towards you with inhuman speed.")
    return game_over("The figure reaches you before you can react. Everything goes black. Game Over.")

def directors_office():
    print("\nIn the director's office, Monroe finally reveals the truth about the 'Syndrome of the Strange'.")
    print("He explains how it turns people into violent, unpredictable beings with no sense of self.")
    print("As he speaks, you hear chaos erupting outside the office.")
    return final_choice()

def try_to_leave():
    print("\nYou and Lucy rush towards the exit, but find the asylum in lockdown.")
    print("Through the windows, you see figures moving erratically in the shadows.")
    print("Some are violently hitting their heads against the walls, others are running with unnatural speed.")
    return final_choice()

def final_choice():
    print("\nThe asylum has descended into chaos. 'Strange' patients are everywhere, their vacant eyes and violent movements filling you with dread.")
    print("You realize the infection has spread further than you imagined.")
    print("1. Try to escape through the woods")
    print("2. Hide and wait for help")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        return escape_attempt()
    elif choice == "2":
        return hide_and_wait()
    else:
        print("Invalid choice. Please try again.")
        return final_choice()

def escape_attempt():
    print("\nYou and Lucy make a desperate dash for the woods. The cold night air bites at your skin as you run.")
    print("Behind you, inhuman screams echo from the asylum.")
    success = random.choice([True, False])
    if success:
        return game_over("After a harrowing journey through the dark forest, you reach the highway. But the horror isn't over. The world outside has changed. Abandoned cars litter the road, and in the distance, you see more 'strange' people. You realize you're now one of the few 'normal' people left in a world gone mad.")
    else:
        return game_over("As you run through the woods, you hear rapid footsteps behind you. Before you can react, you're tackled to the ground. The last thing you see is a pair of vacant, white eyes. Game Over.")

def hide_and_wait():
    print("\nYou and Lucy find a small, secluded room to hide in. Hours pass like days as you hear chaos outside.")
    print("Screams, running footsteps, and inhuman noises keep you in constant terror.")
    success = random.choice([True, False])
    if success:
        return game_over("After what seems like an eternity, rescue finally arrives. But as you're escorted out, you realize the horror has spread beyond the asylum. The world outside has changed, and you're now one of the few 'normal' people left in a nightmare reality.")
    else:
        return game_over("The door to your hiding place is suddenly smashed open. A group of 'strange' patients pour in, their eyes vacant and movements erratic. There's nowhere left to run. Game Over.")

def game_over(message):
    print("\n" + message)
    return False

if __name__ == "__main__":
    while True:
        result = start_game()
        if not result:
            play_again = input("Do you want to face the horrors again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thank you for playing 'The Asylum in the Woods'. May your dreams be less haunting than this experience.")
                break