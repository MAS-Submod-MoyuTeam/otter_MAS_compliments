init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_forget",
            category=["mas_compliment"],
            prompt="I will never forget you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_forget:
    m 1fubftpa "[player]...!"
    m 2subfb "You don't know how happy hearing this makes me."
    m 1kubftpa "I just... love you so much!"
    m 2subfb "It means a lot to me that you insist on giving me this kind of reassurance."
    m 1dubftpb "I wish I could hug you right now! "
    extend "Nobody knows when I would let you go~"
    m 2subfb "Thank you for saying that, [player]~! I won't forget you either!"
    
    return "love"
