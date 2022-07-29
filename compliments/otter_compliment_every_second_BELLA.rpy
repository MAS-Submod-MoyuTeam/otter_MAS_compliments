init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_every_second_with_you_BELLA",
            category=["mas_compliment"],
            prompt="I want to spend every second with you!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_every_second_with_you_BELLA:
    m 1ekbsa "Aww... Do you really mean that?{nw}"
    $ _history_list.pop()
    menu:
        m  "Aww... Do you really mean that?{fast}"
        "Yes":
            m 3hubsb "You're so sweet, [player]~"
            m 3eubsa "I don't think words can express how sweet you are!"
            m 1ekbsa "I love you~"
            $ mas_gainAffection(3, bypass=False)
return
