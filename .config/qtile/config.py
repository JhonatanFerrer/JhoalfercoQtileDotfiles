

#   ____________________________
#  |                           |
#  | Jhoalferco's qtile config |
#  |___________________________|


from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
from colors import *

os.system("bash ~/.config/qtile/autostart.sh")

mod = "mod4"
terminal = "kitty"
webBrowser = "firefox"
fileExplorer = "thunar"
appLauncher = "rofi -show drun"
windowsList = "rofi -show window"
powerMenu = "bash .config/qtile/powermenu.sh"
screenshot = "flameshot gui --clipboard --path Imágenes/Capturas"
screenshotFull = "flameshot full --clipboard --path Imágenes/Capturas"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between different screens
    Key([mod], "space", lazy.next_screen(), desc="Move to the next screen"),


    Key([mod], "return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn(webBrowser), desc="Launch web browser"),
    Key([mod], "e", lazy.spawn(fileExplorer), desc="Launch file explorer"),
    Key([mod], "r", lazy.spawn(appLauncher), desc="Launch app launcher"),
    # Toggle between different layouts as defined below
    Key([mod], "f", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "tab", lazy.spawn(windowsList), desc="Open windows list"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.spawn(powerMenu), desc="Open power menu"),

    # Media controls
    Key([], "print", lazy.spawn(screenshot), desc="Take a screenshot"),
    Key([mod], "print", lazy.spawn(screenshotFull), desc="Take a screenshot of the full desktop"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +5%'), desc="Up the volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -5%'), desc="Down the volume"),
    Key([], "XF86AudioMute", lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle'), desc="Toggle mute"),
    Key([], "XF86AudioMicMute", lazy.spawn('pactl set-source-mute @DEFAULT_SOURCE@ toggle'), desc="Toggle mute the microphone"),
    Key([], "XF86MonBrightnessDown", lazy.spawn('brightnessctl set 5%-'), desc="Down brightness"),
    Key([], "XF86MonBrightnessUp", lazy.spawn('brightnessctl set 5%+'), desc="Up brightness"),  
    Key([], "XF86AudioPlay", lazy.spawn('playerctl play-pause'), desc="Play-pause"),  
    Key([], "XF86AudioNext", lazy.spawn('playerctl next'), desc="Next song"), 
    Key([], "XF86AudioPrev", lazy.spawn('playerctl previous'), desc="Previous song"), 

]

groups = [Group(i) for i in ["1","2","3","4","5"]]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name),),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc="Move focused window to group {}".format(i.name),),
        ]
    )


layouts = [
    layout.Bsp(border_width=0, margin=6, fair=False),
    layout.Max(),
    # layout.Columns(),  
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="UbuntuNerdFont",
    fontsize=14,
    padding=3,
    foreground=foreground,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox("  "),
                widget.GroupBox(
                    highlight_method='line',
                    active=foreground,
                    inactive=foreground_inactive,
                    highlight_color= background, 
                    this_current_screen_border=color1, 
                    this_screen_border=color5, 
                    other_current_screen_border=foreground_inactive, 
                    other_screen_border=foreground_inactive,
                    urgent_border=urgent_color,
                    urgent_text=urgent_color,
                ),
                widget.WindowName(for_current_screen = True),      
                widget.Systray(),
                widget.TextBox(
                    " ", 
                    fontsize=40, 
                    padding=-14, 
                    foreground=color2
                ),
                widget.Volume(
                    mute_format='', 
                    unmute_format='  {volume}%', 
                    step=5,
                    background=color2, 
                    foreground=foreground2
                ),
                # widget.Battery(
                #     charge_char="󱊥",
                #     discharge_char="󱊢",
                #     empty_char="󰂎",
                #     full_char="󱊣",
                #     low_percentage=0.1,
                #     low_background=urgent_color,
                #     low_foreground=foreground2,
                #     format='{char} {percent:2.0%}',
                #     update_interval=2,
                #     background=color2, 
                #     foreground=foreground2
                # ),
                widget.KeyboardLayout(
                    configured_keyboards=['us intl', 'es'],
                    display_map={'us intl': '   us intl',  'es': '   es'},
                    background=color2, foreground=foreground2
                ),
                widget.TextBox(
                    " ",
                    fontsize=40,
                    padding=-14,
                    background=color2,
                    foreground=color3
                ),
                # widget.Wlan(
                #     format='{essid}',
                #     interface='wlp2s0',
                #     disconnected_message='Desconectado',
                #     ethernet_interface='enp1s0f1',
                #     ethernet_message='󰈀',   
                #     background=color3, 
                #     foreground=foreground2
                # ),

                widget.Net(
                    format='{down:6.2f}{down_suffix:<2} {up:6.2f}{up_suffix:<2}',
                    background=color3, 
                    foreground=foreground2
                ),
                widget.TextBox(" ", fontsize=40, padding=-14, background=color3, foreground=color4),
                widget.CPU(
                    format=' {load_percent}% ', 
                    background=color4, 
                    foreground=foreground2
                ),
                widget.Memory(
                    format=' {MemUsed: .0f}{mm}', 
                    background=color4, 
                    foreground=foreground2
                ),
                widget.TextBox(
                    " ", 
                    fontsize=40, 
                    padding=-14, 
                    background=color4, 
                    foreground=color5
                ),
                widget.Clock(
                    format="%a %d/%m %I:%M %p", 
                    background=color5, 
                    foreground=foreground2
                ),
                widget.TextBox(
                    " ", 
                    fontsize=40, 
                    padding=-14, 
                    background=color5, 
                    foreground=color1
                ),
                widget.WidgetBox(
                    widgets=[
                        widget.QuickExit(
                            default_text = ' 󰍃', 
                            countdown_format = ' {}  ', 
                            background=color1, 
                            foreground=foreground2, 

                        ),
                        widget.TextBox(
                            " 󰐥",
                            background=color1, 
                            foreground=foreground2,
                            mouse_callbacks={'Button1':lazy.spawn(powerMenu)}
                            ),
                    ],
                    text_closed=' ',
                    text_open='  ',
                    background=color1, 
                    foreground=foreground2,
                ),
                widget.TextBox("  ", background=color1),
            ],
            28,
            background = background,
            opacity = 0.95,
            margin = [6,6,0,6]
        ),
        
    ),
    Screen(
        top=bar.Bar(
            [
                widget.TextBox("  "),
                widget.GroupBox(
                    highlight_method='line',
                    active=foreground,
                    inactive=foreground_inactive,
                    highlight_color= background, 
                    this_current_screen_border=color1, 
                    this_screen_border=color5, 
                    other_current_screen_border=foreground_inactive, 
                    other_screen_border=foreground_inactive,
                    urgent_border=urgent_color,
                    urgent_text=urgent_color,
                ),
                widget.WindowName(for_current_screen = True),
                widget.TextBox(
                    " ", 
                    fontsize=40, 
                    padding=-14, 
                    foreground=color5
                ),
                widget.Clock(
                    format="%a %d/%m %I:%M %p", 
                    background=color5, 
                    foreground=foreground2
                ),
                widget.TextBox("  ", background=color5),
            ],
            28,
            background = background,
            opacity = 0.95,
            margin = [6,6,0,6]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "qtile"
