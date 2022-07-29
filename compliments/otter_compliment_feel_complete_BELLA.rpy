init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_make_me_feel_complete_BELLA",
            category=["mas_compliment"],
            prompt="You make me feel complete!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_make_me_feel_complete_BELLA:
    if not renpy.seen_label("otter_make_me_feel_complete_BELLA_f"):
        call otter_make_me_feel_complete_BELLA_f from _call_otter_make_me_feel_complete_BELLA_f
    else:
        call otter_make_me_feel_complete_BELLA_s from _call_otter_make_me_feel_complete_BELLA_s
    return

label otter_make_me_feel_complete_BELLA_f:
  m 1ekbsa "Aww, [player]... "
  extend "I could say the same to you!"
  m 3hubsb "I love you so much, [mas_get_player_nickname()]."
  m "You are my best other half~"
  $ mas_gainAffection(3, bypass=True)
return 'love'

label otter_make_me_feel_complete_BELLA_s:
    m 1ekbsa "Thank you, [player]."
    m 3hubsb "You make me feel complete too!"
    m "There's no one else for me but you!"
    $ mas_gainAffection(2, bypass=False)
return
