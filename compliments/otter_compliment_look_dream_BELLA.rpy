init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_look_dream_BELLA",
            category=["mas_compliment"],
            prompt="You look just like a dream.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_look_dream_BELLA:
    m 1dkbsb "[player]..."
    m 1ekbsa "I could say the same. "
    extend 1rkbsa "The time we spend together, our relationship..."
    m 3hkbsb "It all feels like a dream."
    m 3subsb "I never thought I could be this happy."
    m 5hubsu "You are the best [bf]!"
    m 5ekbsu "I love you, [player]~"
return "love"
