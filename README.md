# my dotfiles for Niri WM + Arch Linux :)

![screenshot](https://res.cloudinary.com/dd9nhl1mn/image/upload/v1764099192/screenshot-1764088615_ow7an2.png)

a minimal, cohesive desktop by [hanebox](https://x.com/hanebox) built around the goat of WM -> [niri](https://github.com/YaLTeR/niri) - a scrollable-tiling compositor

## my system (running hot but fine)

- acer swift 14 (intel core ultra 5 / intel arc)
- 16 gigs of ram
- 512 nvme ssd storage
- arch linux + niri (wayland)
- 2880x1800 @ 120hz

_pls buy amd instead_

## must be installed packages

| tool         | description                           |
| ------------ | ------------------------------------- |
| **niri**     | scrollable-tiling wayland compositor  |
| **waybar**   | customizable status bar               |
| **kitty**    | gpu-accelerated terminal (it's fast!) |
| **fuzzel**   | wayland-native app launcher           |
| **mako**     | lightweight notification daemon       |
| **hyprlock** | screen locker                         |
| **wlogout**  | logout/power menu                     |
| **waypaper** | wallpaper manager (using swaybg)      |
| **starship** | cross-shell prompt                    |

## theme

[base2tone mall dark](https://github.com/kovidgoyal/kitty-themes/blob/master/themes/base2tone-mall-dark.conf)

## prerequisites

- arch linux (or arch-based distro)
- wayland-compatible gpu drivers
- a nerd font (configs use hack nerd font / jetbrains mono)

## installation

### 1. install dependencies

```bash
# core packages
sudo pacman -S niri waybar kitty fuzzel mako hyprlock wlogout starship

# additional utilities (important)
sudo pacman -S grim slurp brightnessctl wireplumber pipewire pavucontrol playerctl swaybg swayidle

# aur packages (using yay or paru)
yay -S waypaper
```

**NOTE: no need to install niri if you're already on niri**

### 2. install fonts

```bash
sudo pacman -S otf-commit-mono-nerd  # commit mono nerd font
yay -S otf-commit-mono # commit mono
```

- Commit Mono font family name: "CommitMono"
- Commit Mono Nerd Font family name: "CommitMono Nerd Font"
  > NOTE: this is important to remember so you can use these fonts correctly ;)

### 3. clone the repo

```bash
git clone https://github.com/tfarhan00/dotfiles.git ~/han-dotfiles
cd ~/han-dotfiles
```

### 4. backup existing configs (optional)

```bash
mkdir -p ~/.config-backup
cp -r ~/.config/niri ~/.config/waybar ~/.config/kitty ~/.config/fuzzel \
      ~/.config/mako ~/.config/hyprlock ~/.config/wlogout ~/.config/waypaper \
      ~/.config/starship.toml ~/.config-backup/ 2>/dev/null
```

### 5. copy or replace your config with the new one

example:

```bash
cp -r ~/han-dotfiles/waybar ~/.config/waybar
```

### 6. make waybar media script executable

```bash
chmod +x ~/.config/waybar/media.py
```

### 7. setup starship prompt

add to your `~/.bashrc` or `~/.zshrc`:

```bash
eval "$(starship init bash)"  # for bash
# or
eval "$(starship init zsh)"   # for zsh
```

### 8. setup lockscreen wallpaper

```bash
mkdir -p ~/Pictures/screenlock
# place your lockscreen wallpaper at ~/Pictures/screenlock/main.png (or jpg)
```

### 9. start niri

log out, select "niri" from your display manager, and log back in.

or start from tty:

```bash
niri-session
```

## key bindings

### general

| key                 | action                     |
| ------------------- | -------------------------- |
| `Super + Return`    | open terminal (kitty)      |
| `Super + Space`     | open app launcher (fuzzel) |
| `Super + Q`         | close window               |
| `Super + Shift + E` | quit niri                  |
| `Super + O`         | toggle overview            |

### window navigation

| key                      | action                         |
| ------------------------ | ------------------------------ |
| `Super + H/J/K/L`        | focus left/down/up/right       |
| `Super + Ctrl + H/J/K/L` | move window left/down/up/right |
| `Super + 1-9`            | switch to workspace            |
| `Super + Ctrl + 1-9`     | move window to workspace       |

### window sizing

| key                 | action                              |
| ------------------- | ----------------------------------- |
| `Super + R`         | cycle preset widths (1/3, 1/2, 2/3) |
| `Super + F`         | maximize column                     |
| `Super + Shift + F` | fullscreen window                   |
| `Super + -/=`       | decrease/increase width by 10%      |
| `Super + V`         | toggle floating                     |

### screenshots

| key                 | action                         |
| ------------------- | ------------------------------ |
| `Print`             | screenshot (interactive)       |
| `Ctrl + Print`      | screenshot current screen      |
| `Super + Shift + S` | screenshot region (with slurp) |

### system

| key                  | action              |
| -------------------- | ------------------- |
| `Super + Alt + L`    | lock screen         |
| `XF86Audio*`         | volume controls     |
| `XF86MonBrightness*` | brightness controls |

## waybar modules

- **left**: clock, media player status
- **right**: volume, brightness, battery, network, system tray, power menu

click the power button (`pwr`) to open wlogout.

## customization

### display configuration

edit `~/.config/niri/config.kdl` to configure your monitors:

```kdl
output "eDP-1" {
    mode "2880x1800@120"
    scale 2
    position x=0 y=0
}
```

run `niri msg outputs` to list available outputs.

### idle/lock behavior

the config includes swayidle for automatic screen dimming, locking, and suspend:

- 10 min: dim screen to 10%
- 10 min: lock screen
- 20 min: turn off monitors + suspend

### window rules

nautilus and imv open as floating windows by default. edit the `window-rule` sections in `config.kdl` to customize.

## troubleshooting

### apps not using wayland

the niri config sets environment variables to force wayland for most toolkits. if an app still uses xwayland, check:

- `QT_QPA_PLATFORM`
- `GDK_BACKEND`
- `ELECTRON_OZONE_PLATFORM_HINT`

### waybar not showing

ensure waybar is running:

```bash
waybar &
```

or reload niri config: `niri msg action reload-config`

### notifications not working

restart mako:

```bash
pkill mako && mako &
```

## credits

- [niri](https://github.com/YaLTeR/niri) - scrollable-tiling wayland compositor
- [dimmed monokai](https://github.com/distantcam/DistantVim) - color scheme inspiration
- [starship](https://starship.rs) - cross-shell prompt

---

feel free to reach out if you have any questions or just wanna chat about linux stuff! hit me up on X [@hanebox](https://x.com/hanebox) :)
