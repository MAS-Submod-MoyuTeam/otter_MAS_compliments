init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_make_happy",
            category=["mas_compliment"],
            prompt="You make me really happy...",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_make_happy:
    m 1dubfa "[player]..."
    m 5fubfb "I have said it already, but you know you make me the happiest girl in the world, right?"
    m 5hubfa "I love you..."
    m 4kubfa "And I'll be here to make you happy every single day."
    m 4subfa "For the rest of our lives!"
    m 1mubfb "Eternity is too little time for us."
    m 5fsbfa "I absolutely adore you."
    return "love"
