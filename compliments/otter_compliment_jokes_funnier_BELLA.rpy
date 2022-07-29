init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_jokes_funnier_BELLA",
            category=["mas_compliment"],
            prompt="Jokes are way funnier when you tell them!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_jokes_funnier_BELLA:
    m 1hub "Aww~ Thanks, [player]!"
    m 7mkblb "You keep spoiling me with all these compliments, ehehe."
    m 3ekb "I love making you laugh!"
    m 5rublb "Just imagining the sound of your laugh..."
    m 4hubla "Is already enough to make me smile."
    m "I love you!"
return "love"
