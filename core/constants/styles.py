import os
base = os.getcwd()

MAIN_STYLE = f"""
#main_frame {{
    background-color: black;
}}

#music_button,
#utility_button,
#nav_button,
#diag_button {{
    border: 1px solid #000000;
    border-radius: 6px;
    border-style: inset;
    background-color: rgba(30%, 30%, 30%);
    min-width: 80px;
}}

#music_button {{
    background-image: url({base}/res/icons/music.png);
    background-position: center;
    background-repeat: no-repeat;
}}

#music_button:pressed,
#utility_button:pressed,
#nav_button:pressed,
#diag_button:pressed {{
    background-color: rgba(20%, 20%, 20%);
}}

"""

# #music_button, #utility_button, #nav_button, #diag_button {{
#     border: 2px solid #8f8f91;
#     border-radius: 6px;
# }}

