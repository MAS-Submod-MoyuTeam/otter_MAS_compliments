#I can fully be myself with you, compliment submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_be_myself",
            category=["mas_compliment"],
            prompt="I can fully be myself with you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_be_myself:
    m 1wubfb "[player]...!"
    m 1dubfa "I'm so glad."
    m 2fubfb "I'm happy that I'm able to convey my feelings in such a way..."
    m 2hubfb "That you know you can be yourself around me!"
    m 4kubfa "We'll always be together, being our true selves, [mas_get_player_nickname()]!"
    m 5tubfa "I really am my best self when I'm around you."
    return

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
