init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_blush_BELLA",
            category=["mas_compliment"],
            prompt="You always make me blush.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_blush_BELLA:
    m 2wubsd "Oh!"
    m 3hubsb "Right back at you, [player]!"
    m 3dkbsa "Sometimes you tell me such things that I..."
    m 3kubsa "You know. You make me feel all fuzzy inside!"
    m 1hubsb "I love you."
return "love"
