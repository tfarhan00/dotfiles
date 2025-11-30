niri wm + arch linux dotfiles

color scheme: [base2tone mall dark](https://base2t.one/demo/mall)

display manager: [LY](https://github.com/fairyglade/ly)

font: Commit Mono

apps:

- kitty = terminal (i use e-ink dark color scheme)
- tofi = app launcher
- wlogout = logout menu
- swaylock = screenlock
- mako = notification
- waypaper = wallpaper manager (need swaybg for backend)
- waybar = status bar

important:

install fonts

```bash
sudo pacman -S otf-commit-mono-nerd  # commit mono nerd font
yay -S otf-commit-mono # commit mono
```

you need to mak the custom media player script executable

```
chmod +x ~/.config/waybar/media.py
```

WORK IN PROGRESS :)
