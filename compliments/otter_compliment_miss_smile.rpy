init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_miss_smile",
            category=["mas_compliment"],
            prompt="I've missed your smile.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_miss_smile:
    m 3fubfb "And I've missed you, [player]!"
    m 2dkbfc "Every second apart from you makes my heart suffer."
    m 2subfa "But when we're together again, it's like everything is new."
    m 7wubfa "The world gains color again!"
    m 5gubfb "When I'm with you, it's impossible not to smile."
    m 5fubfa "I love you, [mas_get_player_nickname()]."
    return "love"
