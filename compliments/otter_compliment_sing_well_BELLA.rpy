init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_sing_well_BELLA",
            category=["mas_compliment"],
            prompt="You sing so well!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_sing_well_BELLA:
    m 1hua "You really think so, [player]?"
    m 2eka "Sometimes you even catch me off guard, singing to myself..."
    m 3hkb "I feel so embarrassed!"
    m 3eka "..."
    m 1eua "But I really trust you even with my own thoughts."
    m 7hub "I mean, I feel comfortable around you!"
    m 5tubla "I love you, [mas_get_player_nickname()]."
return "love"
