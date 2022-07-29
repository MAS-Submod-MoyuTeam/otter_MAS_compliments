init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_light_any_room_BELLA",
            category=["mas_compliment"],
            prompt="You light up every room just by smiling.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_light_any_room_BELLA:
    if not renpy.seen_label("otter_light_any_room_BELLA_f"):
        call otter_light_any_room_BELLA_f from _call_otter_light_any_room_BELLA_f
    else:
        call otter_light_any_room_BELLA_s from _call_otter_light_any_room_BELLA_s
    return

label otter_light_any_room_BELLA_f:
    m 2hkbsa "Just when I thought you couldn't be any sweeter..."
    m 3hub "Ahaha!"
    m 5tkbsa "Heh, I already knew that but thanks for reminding me, my dear~{nw}"
    $ _history_list.pop()
    menu:
        m  "Heh, I already knew that but thanks for reminding me, my dear~{fast}"
        "I'm glad you're aware :)":
            m 5hubsb "You are amazing, [mas_get_player_nickname()]!"
            m 5ekbsu "I love you~"
            $ mas_gainAffection(3, bypass=True)

        "...":
            m 5ekbsu "I love you~"
            $ mas_gainAffection(2, bypass=True)

        "No":
            m 1wuc "W--What?"
            m 2ekc "[player]...{nw}"
            $ _history_list.pop()
            menu:
                m "[player]...{fast}"
                
                "I'm just kidding ;)":
                    m 1hksdlb "Stop teasing like me like that, ehehe~"
                    m 1euu "I love you~"
                    $ mas_gainAffection(1, bypass=True)
                        
return 'love'

label otter_light_any_room_BELLA_s:
    m 1ekbsa "Thank you so much for reminding me, [player]..."
    m "You're such a sweetheart~"
    m "I love you!"
    $ mas_gainAffection(1, bypass=False)
return "love"
