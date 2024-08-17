
#set the xrandr according your needs :3

xrandr --output DP-1 --pos 0x0 --mode 1920x1080 --rate 60 --rotate right --rate 60 --output HDMI-2 --pos 1080x480 --mode 1920x1080 --rate 100 --primary
# xrandr --output eDP-1 --pos 0x0 --mode 1366x768 --rate 60 --primary &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/dunst &
picom &
nitrogen --restore &


