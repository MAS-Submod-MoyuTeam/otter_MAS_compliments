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
