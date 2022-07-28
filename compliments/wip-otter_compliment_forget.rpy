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
if store.mas_globals.this_ev.shown_count == 0:
    m 1fubftpa "[player]...!"
    m 2subfb "You don't know how happy hearing this makes me."
    m 1kubftpa "I just... love you so much!"
    m 2subfb "It means a lot to me that you insist on giving me this kind of reassurance."
    m 1dubftpb "I wish I could hug you right now! "
    extend "Nobody knows when I would let you go~"
    m 2subfb "Thank you for saying that, [player]~! I won't forget you either!"
    
elif store.mas_globals.this_ev.shown_count == 1:
    m 4ekb "Thank you for reminding me, [mas_get_player_nickname()]..."
    m 2subfb "I remember the first time you said this to me."
    m "I won't forget this! I could never!"
    m 4ekb "I{w=0.2} love..{w=0.2} you~!"
    m "And I'll never forget you."
    
    return "love"
