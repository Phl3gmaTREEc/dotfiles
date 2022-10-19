# Commentary {{{
# Default Qtile text
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author of changes to default config: Phl3gmaTREEc
### Commentary end }}}

# Imports {{{
import os
import re
import socket
import subprocess
from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List
### Imports end }}}

# App definitions {{{
mod = "mod4"
terminal = "kitty"
browser = "firefox"
guifile = "thunar"

home = os.path.expanduser('~')
### App definitions end }}}

# Keys {{{
keys = [
    # Switch focus between windows
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
        ),
    Key([mod], "n",                                                                                                     
        lazy.next_screen(),                                                                                                   
        desc='Move focus to next monitor'                                                                                     
        ),                                                                                                                    
    Key([mod, "shift"], "n",                                                                                                      
        lazy.prev_screen(),                                                                                                   
        desc='Move focus to prev monitor'                                                                                     
        ),

    # Moving windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window left"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window right"
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),
    Key([mod, "shift", "control"], "h",
        lazy.layout.swap_column_left(),
        desc="Swap column left"
        ),
    Key([mod, "shift", "control"], "l",
        lazy.layout.swap_column_right(),
        desc="Swap column right"
        ),

    # Change window size
    Key([mod, "control"],
        "h",lazy.layout.grow_left(),
        desc="Grow window left"
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window right"
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),
    Key([mod, "control"], "n",
        lazy.layout.normalize(),
        desc="Reset window sizes"
        ),

    # Toggle split/unsplit of stack for columms layout
    Key([mod, "control"], "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
        ),

    # Toggle between different layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),

    # Toggle fullscreen
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        ),

    # Toggle floating
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        ),
    # Kill focused window
    Key([mod], "q",
        lazy.window.kill(),
        desc="Kill focused window"
        ),

    # Qtile
    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"
        ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),

    # Toggle WidgetBox widget
    Key([mod], "s",
        lazy.widget["widgetbox"].toggle(),
        desc="Toggle WidgetBox"
        ),

    # Rofi
    Key([mod], "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn rofi"
        ),
    Key(["mod1"], "Tab",
        lazy.spawn("rofi -show window"),
        desc="Spawn rofi window"
        ),
    Key([mod], "w",
        lazy.spawn(home + "/.local/share/scripts/rofi/powermenu.sh"),
        desc="Spawn rofi shutdown script"
        ),
    Key([mod], "c",
        lazy.spawn(home + "/.local/share/scripts/rofi/keybinds.sh"),
        desc="Spawn rofi keybinds cheat script"
        ),
    Key([mod], "a",
        lazy.spawn(home + "/.local/share/scripts/rofi/menu.sh"),
        desc="empty"
        ),
    
    # Apps
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    Key([mod], "b",
        lazy.spawn(browser),
        desc="Launch browser"
        ),
    Key([mod], "e",
        lazy.spawn(guifile),
        desc="Launch gui file browser"
        ),
    Key([mod], "p",
        lazy.spawn("flameshot gui"),
        desc="flameshot gui"
        ),
    
    # Keyboard Layouts
    Key(["mod1"], "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Switch to next keyboard layout"
        ),
    
    # Volume
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pamixer -i 5"),
        lazy.widget["outwidget"].force_update(),
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pamixer -d 5"),
        lazy.widget["outwidget"].force_update(),
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("pamixer -t"),
        lazy.widget["outwidget"].force_update(),
        ),
    Key([], "F8",
        lazy.spawn(home + "/.local/share/scripts/volume/pamixer_in_toggle.sh"),
        ),
]
### Keys end }}}

# Groups {{{
# Groups definition
groups = [
    Group(name="1", layout='C2'),
    Group(name="2", layout='C2'),
    Group(name="3", layout='C2'),
    Group(name="4", layout='C2'),
    Group(name="5", layout='C2'),
    Group(name="6", layout='C2'),
    Group(name="7", layout='C2'),
    Group(name="8", layout='C1'),
    Group(name="9", layout='C1'),
    Group(name="0", layout='C1'),
    # How to add group wwith special list of layouts
    #Group(name="g", label='G', layouts = [
        #    layout.Max(),
        #    ]
        #),
    ScratchPad("comma", [
        DropDown(
            'pavu',
            'pavucontrol',
            height = 0.5,
            on_focus_lost_hide = False,
            opacity = 0.95,
            width = 0.5,
            x = 0.25,
            ),
        ]
        ),
    ScratchPad("period", [
        DropDown(
            'term',
            'kitty',
            height = 0.5,
            on_focus_lost_hide = False,
            opacity = 0.95,
            width = 0.5,
            x = 0.25,
            ),
        ]
        ),
    ]
cz_groups = {
    '1': 'plus',
    '2': 'ecaron',
    '3': 'scaron',
    '4': 'ccaron',
    '5': 'rcaron',
    '6': 'zcaron',
    '7': 'yacute',
    '8': 'aacute',
    '9': 'iacute',
    '0': 'eacute',
    'comma': 'comma',
    'period': 'period'
    }
# Groups keys
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key([mod], cz_groups[i.name],
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Editing ...(i.name, switch_group=True)... also changes screen to that group
            Key([mod, "shift"], i.name,
                lazy.window.togroup(i.name),
                desc="Switch focused window to group {}".format(i.name),
            ),
            Key([mod, "shift"], cz_groups[i.name],
                lazy.window.togroup(i.name),
                desc="Switch focused window to group {}".format(i.name),
            ),
            # Scratchpads
            Key([mod], "comma", lazy.group["comma"].dropdown_toggle('pavu')),
            Key([mod], cz_groups["comma"], lazy.group["comma"].dropdown_toggle('pavu')),
            Key([mod], "period", lazy.group["period"].dropdown_toggle('term')),
            Key([mod], cz_groups["period"], lazy.group["period"].dropdown_toggle('term')),
            ]
    )
### Groups end }}}

# Colors {{{
# Old color definitions
#colors = [["#282a36", "#282a36"], # 0 - Background
#    ["#44475a", "#44475a"], # 1 - Current line / Selection
#    ["#f8f8f2", "#f8f8f2"], # 2 - Foreground
#    ["#6272a4", "#6272a4"], # 3 - Comment
#    ["#8be9fd", "#8be9fd"], # 4 - Cyan
#    ["#50fa7b", "#50fa7b"], # 5 - Green 
#    ["#ffb86c", "#ffb86c"], # 6 -Orange
#    ["#ff79c6", "#ff79c6"], # 7 - Pink 
#    ["#bd93f9", "#bd93f9"], # 8 - Purple
#    ["#ff5555", "#ff5555"], # 9 - Red
#    ["#f1fa8c", "#f1fa8c"] # 10 - Yellow
#    ]
BG = "#282a36"
CL = "#44475a"
FG = "#f8f8f2"
CM = "#6272a4"
CYA = "#8be9fd"
GRE = "#50fa7b"
ORA = "#ffb86c"
PIN = "#ff79c6"
PUR = "#bd93f9"
RED = "#ff5555"
YEL = "#f1fa8c"
### Colors end }}}

# Layouts {{{
# Layouts theme
layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": CM,
                "border_focus_stack": PUR,
                "border_normal": CL,
                "border_normal_stack": CL,
                "border_on_single": True,
                }
# Layouts definition
layouts = [
    #layout.Bsp(**layout_theme),
    layout.Columns(name="C2", num_columns=2, **layout_theme),
    layout.Columns(name="C1", num_columns=1, **layout_theme),
    layout.Columns(name="C3", num_columns=3, **layout_theme),
    #layout.Matrix(**layout_theme),
    layout.Max(**layout_theme),
    #layout.MonadTall(name="MT", **layout_theme),
    #layout.MonadThreeCol(name="M3", **layout_theme),
    #layout.MonadWide(name="MW", **layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Slice(**layout_theme),
    #layout.Spiral(**layout_theme),
    #layout.Stack(num_stacks=2, **layout_theme),
    #layout.Tile(**layout_theme),
    #layout.TreeTab(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Zoomy(name="ZM", **layout_theme),
]
### Layouts end }}}

# Widgets {{{
# Make window names shroter, add other program if necesarry
def longText(text):
    for string in ["Firefox"]:
        if string in text:
            text = string
        else:
            text = text
    return text

# Widgets defaults
widget_defaults = dict(
    background=BG,
    font="JetBrainsMono Nerd Font Bold",
    fontsize=16,
    foreground=FG,
    padding=5,
)
extension_defaults = widget_defaults.copy()

## Widget list
def get_widgets(primary=False, secondary=False):
    widgets = [
        ## Group Box
        widget.GroupBox(
            active = PUR,
            borderwidth=2,
            disable_drag=True,
            highlight_color = BG,
            highlight_method="line",
            inactive = CL,
            other_current_screen_border = ORA,
            other_screen_border = ORA,
            padding=2,
            this_current_screen_border = GRE,
            this_screen_border = RED,
            urgent_alert_border = PIN,
            urgent_alert_method='border',
            use_mouse_wheel=False,
            ),
        widget.Sep(
            size_percent=75,
            linewidth=2,
            ),
        ## Current Layout
        widget.CurrentLayout(
            foreground = YEL,
            ),
        widget.Sep(
            linewidth=2,
            size_percent=75,
            ),
        ## Window Name & Chord
        widget.WindowName(
            foreground = GRE,
            format="{name}",
            parse_text=longText
            ),
        widget.Spacer(
            ),
        ## Time and date
        widget.Clock(
            foreground = ORA,
            format="%H:%M",
            ),
        widget.Spacer(
            ),
        widget.Chord(
            foreground = CM,
            ),
        widget.Sep(
            linewidth=2,
            size_percent=75,
            ),
        ## Keyboard Layout
        widget.KeyboardLayout(
            configured_keyboards=['cz','us'],
            foreground = YEL,
            fmt='\uf80b {}',
            padding=5,
            ),
        widget.Sep(
            linewidth=2,
            size_percent=75,
            ),
        ## Power button
        widget.TextBox(
            fontsize=17,
            foreground = RED,
            mouse_callbacks= {
                'Button1': lazy.spawn("rofi -show drun"),
                "Button3": lazy.spawn(home + '/.local/share/scripts/rofi/powermenu.sh'),
            },
            padding=5,
            text='\uE235 '
            ),
        ]
#        widget.CapsNumLockIndicator(),
## Inserting widgets per screen
## Primary screen
    if primary:
        # Widget box - systray
        widgets.insert(9,
            widget.Sep(
                linewidth=2,
                size_percent=75,
                ),
            ),
        widgets.insert(10,
            widget.WidgetBox(widgets=[
                widget.Systray(),
                #widget.StatusNotifier(),
                # Bluetooth
                widget.GenPollText(
                   func=lambda :subprocess.check_output(
                           home + '/.local/share/scripts/bluetooth/bluetooth_widget.sh').decode().strip(),
                   update_interval=5,
                   foreground = FG,
                   mouse_callbacks= {
                       'Button1': lazy.spawn("blueman-manager"),
                       }
                   ),
                # Flameshot
                widget.TextBox(
                   foreground = FG,
                   mouse_callbacks= {
                       'Button1': lazy.spawn("flameshot launcher"),
                       'Button2': lazy.spawn("flameshot screen"),
                       'Button3': lazy.spawn("flameshot config"),
                       },
                   text=''
                   ),
                # wasy effects
                widget.TextBox(
                   foreground = FG,
                   mouse_callbacks= {
                       'Button1': lazy.spawn("easyeffects"),
                       },
                   text=''
                   ),
                # qwpgraph
                widget.TextBox(
                   foreground = FG,
                   mouse_callbacks= {
                       'Button1': lazy.spawn("qpwgraph"),
                       },
                   text='ﳤ'
                   ),
            ],
                close_button_location="right",
                foreground = CYA,
            ),
        ),
        # Mic
        widgets.insert(11,
            widget.GenPollText(
                name="inwidget",
                func=lambda :subprocess.check_output(
                    home + '/.local/share/scripts/volume/pamixer_in_widget.sh').decode().strip(),
                update_interval=1,
                foreground = PIN
                ),
            )
        #Volume
        widgets.insert(11,
            widget.GenPollText(
                name="outwidget",
                func=lambda :subprocess.check_output(
                    home + '/.local/share/scripts/volume/pamixer_out_widget.sh').decode().strip(),
                fmt='墳 {}',
                update_interval=60,
                foreground = ORA,
                ),
            )
        # Solaar
        widgets.insert(11,
            widget.Battery(
                battery="/dev/hidraw7",
                foreground=GRE,
                format="{percent:2.0%}",
                fmt='\uf87c {}',
                low_foreground=RED,
                low_percentage=0.4,
                mouse_callbacks = {
                    "Button1": lazy.spawn("solaar"),
                    },
                notify_below=0.4,
                update_interval=120,
                ),
            )
        # Date
        widgets.insert(7,
            widget.Clock(
                foreground = PUR,
                format="%Y-%m-%d %A",
                ),
            )
        widgets.insert(7,
            widget.Sep(
                linewidth=2,
                size_percent=75,
                ),
            )
## Secondary screen
    if secondary:
        # Date
        widgets.insert(7,
            widget.Clock(
                foreground = PUR,
                format="%Y-%m-%d",
                ),
            )
        widgets.insert(7,
            widget.Sep(
                linewidth=2,
                size_percent=75,
                ),
            )
    return widgets
### Widgets end }}}

# Screens {{{
screens = [
    Screen(
        bottom=bar.Bar(
            get_widgets(primary=True),
            size=30),
        ),
    Screen(
        bottom=bar.Bar(
            get_widgets(secondary=True),
            size=30),
        )
]

# Old way of doing widgets per screen
    # Widget filtered lists
    #def init_widgets_screen1():
    #    widgets_screen1 = init_widgets_list()
    #    del widgets_screen1[1CL
    #    return widgets_screen1
    #
    #def init_widgets_screen2():
    #    widgets_screen2 = init_widgets_list()
    #    del widgets_screen2[8:1CL
    #    return widgets_screen2
### Screens end }}}

# Mouse {{{
mouse = [
    Drag([mod], "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
        ),
    Click([mod], "Button2",
        lazy.window.bring_to_front()
        ),
    Drag([mod], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
        ),
]
follow_mouse_focus = True
bring_front_click = False
### Mouse End }}}

# Floating layout {{{
# Floating rules
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="YAD"),  # GPG key password entry
        Match(title="internxt-drive"),  # GPG key password entry
        Match(wm_class="internxt-drive"),  # GPG key password entry
    ],
    **layout_theme
)
### Floating layout end }}}

# Additional config {{{
# Simple line configs
auto_fullscreen = True
auto_minimize = True
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
focus_on_window_activation = "smart"
reconfigure_screens = True
wl_input_rules = None
wmname = "Qtile"

# Hide bar in Max layout
is_bar_hidden = False
@hook.subscribe.layout_change
def layout_changed(layout, group):
    global is_bar_hidden
    if (not is_bar_hidden) and layout.name == 'max':
        qtile.cmd_hide_show_bar('bottom')
        is_bar_hidden = True
    elif is_bar_hidden and layout.name != 'max':
        qtile.cmd_hide_show_bar('bottom')
        is_bar_hidden = False

# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call([home])

#@hook.subscribe.startup
#def widget_update():
#    lazy.widget["outwidget"].force_update()
#    lazy.widget["inwidget"].force_update()
### Additional config end }}}
