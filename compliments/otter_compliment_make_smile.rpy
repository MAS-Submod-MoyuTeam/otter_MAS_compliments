init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_make_smile",
            category=["mas_compliment"],
            prompt="You always make me smile!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_make_smile:
    m 1gubfa "..."
    m 1hubfb "Gosh, its the same for me!"
    m 1wubfb "See? " 
    extend 1hubfa "I can't stop smiling!"
    m 1hubfb "Ahahaha~"
    m 5fubfa "I can't stop loving you this desperately, [player]."
    m 5kubfa "You just make it impossible not to."
    m 5tubfa "I loooooooove you!"
    return "love"
