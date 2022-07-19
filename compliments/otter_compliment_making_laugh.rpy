init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_making_laugh",
            category=["mas_compliment"],
            prompt="I love making you laugh.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_making_laugh:
    m 5tubfa "Is that right, [player]?"
    m 2mubfb "Well, I can't wait to cross over..."
    m 2hubfb "And make you laugh over and over!"
    m 7lubfa "From tickling, from my awesome jokes, from everything!"
    m 7kubfa "Seeing you smile will be the high point of every day."
    m 3fubfb "My little sunshine."
    return
