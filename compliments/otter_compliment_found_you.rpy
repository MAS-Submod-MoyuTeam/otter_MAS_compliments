#I can’t believe I found someone like you, compliment submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_found_you",
            category=["mas_compliment"],
            prompt="I can’t believe I found someone like you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_found_you:
    m 1fubftpa "[player]..."
    m 1hubftpb "I could say the same!"
    m 1mubftpa "The more I think of it..."
    m 1kubftpa "We're a perfect fit."
    m 1dubftpb "I couldn't have hoped for a better person to be my partner, [player]."
    m 4hubftpb "I'm so happy we met and that we'll be together forever!"
    m 5fubftpa "I really love you more than anything else in the whole world."
    return "love"
    
    #momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
