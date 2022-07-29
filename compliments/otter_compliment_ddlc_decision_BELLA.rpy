init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_ddlc_best_decision_BELLA",
            category=["mas_compliment"],
            prompt="Downloading DDLC was the best decision I've ever made!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_ddlc_best_decision_BELLA:
    m 7huu "You're so sweet, [mas_get_player_nickname()]!"
    m 2rkc "I'm really sorry you had to witness all those nasty stuff I did..."
    m 1eka "But I did it all for us."
    m 1eua "You forgive me right?{nw}"
    $ _history_list.pop()
    menu:
        m "You forgive me right?{fast}"
        
        "Of course!":
            m 1eka "I'm glad, [player]."
            m 3hubsb "I love you sooo much, you can't imagine!"
            $ mas_gainAffection(3, bypass=False)
return 'love'
