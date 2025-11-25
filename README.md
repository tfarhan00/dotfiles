# my dotfiles for niri wm + arch linux :)

![screenshot](https://res.cloudinary.com/dd9nhl1mn/image/upload/v1764044525/screenshot-1764043829_ppfudh.png)

a minimal, cohesive wayland desktop built around [niri](https://github.com/YaLTeR/niri) - a scrollable-tiling compositor.

## my system

- acer swift 14 (intel core ultra 5 / intel arc)
- arch linux + niri (wayland)
- 2880x1800 @ 120hz

## what's included

| tool         | description                                   |
| ------------ | --------------------------------------------- |
| **niri**     | scrollable-tiling wayland compositor          |
| **waybar**   | customizable status bar                       |
| **kitty**    | gpu-accelerated terminal (it's fast!)         |
| **fuzzel**   | wayland-native app launcher                   |
| **mako**     | lightweight notification daemon               |
| **swaylock** | screen locker                                 |
| **wlogout**  | logout/power menu                             |
| **waypaper** | wallpaper manager (using swaybg)              |
| **starship** | cross-shell prompt                            |
| **glow**     | terminal markdown viewer (simple and pretty!) |

## theme

dimmed monokai color scheme for mostly terminal and bar (planning to make it as system wide as possible)

- background: `#1e1e1e`
- foreground: `#b8bcb9`
- accent: `#568ea3` (blue), `#c37033` (orange)

## prerequisites

- arch linux (or arch-based distro)
- wayland-compatible gpu drivers
- a nerd font (configs use hack nerd font / jetbrains mono)

## installation

### 1. install dependencies

```bash
# core packages
sudo pacman -S niri waybar kitty fuzzel mako swaylock wlogout glow starship

# additional utilities
sudo pacman -S grim slurp brightnessctl wireplumber pipewire pavucontrol

# aur packages (using yay or paru)
yay -S waypaper swaybg swayidle
```

### 2. install fonts

```bash
sudo pacman -S ttf-hack-nerd ttf-jetbrains-mono-nerd
```

### 3. clone the repo

```bash
git clone https://github.com/yourusername/dotfiles.git ~/Developer/dotfiles
cd ~/Developer/dotfiles
```

### 4. backup existing configs (optional)

```bash
mkdir -p ~/.config-backup
cp -r ~/.config/niri ~/.config/waybar ~/.config/kitty ~/.config/fuzzel \
      ~/.config/mako ~/.config/swaylock ~/.config/wlogout ~/.config/waypaper \
      ~/.config/glow ~/.config/starship.toml ~/.config-backup/ 2>/dev/null
```

### 5. create symlinks

```bash
# create config directory if needed
mkdir -p ~/.config

# symlink all configs
ln -sf ~/Developer/dotfiles/.config/niri ~/.config/niri
ln -sf ~/Developer/dotfiles/.config/waybar ~/.config/waybar
ln -sf ~/Developer/dotfiles/.config/kitty ~/.config/kitty
ln -sf ~/Developer/dotfiles/.config/fuzzel ~/.config/fuzzel
ln -sf ~/Developer/dotfiles/.config/mako ~/.config/mako
ln -sf ~/Developer/dotfiles/.config/swaylock ~/.config/swaylock
ln -sf ~/Developer/dotfiles/.config/wlogout ~/.config/wlogout
ln -sf ~/Developer/dotfiles/.config/waypaper ~/.config/waypaper
ln -sf ~/Developer/dotfiles/.config/glow ~/.config/glow
ln -sf ~/Developer/dotfiles/.config/starship.toml ~/.config/starship.toml
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
mkdir -p ~/Pictures
# place your lockscreen wallpaper at ~/Pictures/screenlock.png
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
