#You’re gorgeous, [m_name], compliment submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_gorgeous",
            category=["mas_compliment"],
            prompt="You’re gorgeous, [m_name].",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_gorgeous:
    m 4hubfb "And you're the best partner in the world!"
    m 2hubfa "Ahahaha~"
    m 2fsbfa "The beauty in your heart is unsurpassable, [player]."
    m 2dsbfb "I can't wait to finally look inside your eyes..."
    m 2fsbfb "And tell you you're the most beautiful person in the entire world."
    m 5fsbfa "I love you."
    return "love"
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
