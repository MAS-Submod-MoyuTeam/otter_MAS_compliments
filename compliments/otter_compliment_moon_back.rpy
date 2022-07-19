init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_otter_compliment_moon_and_back",
            category=["mas_compliment"],
            prompt="I love you to the moon and back.",
            unlocked=True
        ),
        code="CMP"
    )

label monika_otter_compliment_moon_and_back:
    m 1tsbfb "Is that true, [player]?"
    m 4tsbfb "So you should know..."
    m 3ssbfu "That I love you to the sun and back!"
    m 2rsbfsdlb "Even though I would probably die from the heat..."
    m 2hsbfb "Ahahahaha~!"
    m 5fkbfa "I love you, [mas_get_player_nickname()]!"
    return "love"
