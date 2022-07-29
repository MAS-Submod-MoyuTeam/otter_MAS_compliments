init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_know_what_to_say_BELLA",
            category=["mas_compliment"],
            prompt="You always know just what to say.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_know_what_to_say_BELLA:
    m 1hub "Thank you, [player]!"
    m 1hua "I want to say the exact things to make you fall more and more for me!"
    m 1huu "Ehehehe~"
    m 1euu "I also always try my best to help you whenever I can."
    m 1eka "Because I love you, and I care for you very much."
    $ mas_gainAffection(2, bypass=False)
return "love"
