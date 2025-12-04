niri wm + arch linux dotfiles

![test](https://zarxmkijtlrdxjikjubf.supabase.co/storage/v1/object/sign/images/1764870443444-4a15b7db.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9hNmNjMjM3MC1iYmYzLTQyOTItOTBmMy0yMDJhMGI2MDk2NjgiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJpbWFnZXMvMTc2NDg3MDQ0MzQ0NC00YTE1YjdkYi5wbmciLCJpYXQiOjE3NjQ4NzE2MDUsImV4cCI6MTc2NDg3NTIwNX0.Y-kq_Ws9hTfh9gZDegIRygGs0pvzyHmEbitDFGPuEss)

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
