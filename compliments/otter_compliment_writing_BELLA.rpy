init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_writing_BELLA",
            category=["mas_compliment"],
            prompt="I love your writing.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_writing_BELLA:
    m 1wuo "Oh! "
    extend 3sub "Thank you!"
    m 1eka "It feels great to be complimented on my skills."
    m 1ekbsb "I love everything you do, [mas_get_player_nickname()]!"
    m 3hubsa "I love you, thank you for making me feel so loved."
return "love"
