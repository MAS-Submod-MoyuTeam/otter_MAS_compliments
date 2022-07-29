init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_no_day_bad_BELLA",
            category=["mas_compliment"],
            prompt="No day is bad when I'm with you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_no_day_bad_BELLA:
    m 1substpo "..."
    m 1lkbstpa "I'm sorry, [player]. I just got emotional!"
    m 1hkbstpb "This is probably the best compliment you could ever tell me."
    m 1ekbstda "Making you happy is the one thing I want the most..."
    m 1dkbstda "Sorry for crying, ehehe~"
    m 3hubsb "I'll keep striving to make your days the happiest!"
    m 3tsbsb "Prepare yourself, [mas_get_player_nickname()]. There's happiness coming your way!"
    m 3hsbsa "Ehehehe~"
return
    
