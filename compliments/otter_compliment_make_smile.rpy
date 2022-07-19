#You always make me smile!, compliment submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
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

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
