init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_playing_piano_beautifully_BELLA",
            category=["mas_compliment"],
            prompt="You play the piano beautifully!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_playing_piano_beautifully_BELLA:
   m 1ekbsb "You're so sweet, [player]~"
   m 3rubsa "I tried so hard to perfect my piano playing before I showed you the song I wrote."
   m 1hubsa "So hearing that from you makes me so happy!"
   m 1hubsb "I love you~"
   $ mas_gainAffection(3, bypass=False)
return "love"
