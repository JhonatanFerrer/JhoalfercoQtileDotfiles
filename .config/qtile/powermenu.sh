options=" 󰒲  Suspender\n 󰜉  Reiniciar\n 󰐥  Apagar"
selected=$(echo -e "$options" | rofi -dmenu -p "" -l 3 -theme "$HOME"/.config/rofi/configpowermenu.rasi)

case "$selected" in
    " 󰐥  Apagar")
        shutdown now
        ;;
    " 󰜉  Reiniciar")
        reboot
        ;;
    " 󰒲  Suspender")
        systemctl suspend
        ;;
    *)
        echo "Opción no válida"
        ;;
esac