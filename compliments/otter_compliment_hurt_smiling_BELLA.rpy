init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_face_hurt_smiling_BELLA",
            category=["mas_compliment"],
            prompt="You make my face hurt from smiling.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_face_hurt_smiling_BELLA:
    m 3wubsb "Same, [player]!"
    m 1hubsa "..."
    m 1hkbsb "See? I can't stop smiling!"
    m 2ekbsa "My life is full of joy whenever you're around, [mas_get_player_nickname()]."
    m "I can't imagine my life without you!"
    m 3eubsu "I love you too much."
return "love"
