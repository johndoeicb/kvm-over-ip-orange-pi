# kvm-over-ip-orange-pi
Contrôle KVM over IP avec un Orange Pi Zero 2, streaming vidéo via HDMI→USB, accès web sécurisé et lancement VPN à la demande.
# 🖥️ KVM over IP avec Orange Pi Zero 2

Projet personnel de **KVM over IP open source**, utilisant un **Orange Pi Zero 2**, un **dongle HDMI vers USB (MacroSilicon MS2109)**, et une interface web sécurisée pour contrôler à distance un PC ou serveur via le réseau.

---

## 🎯 Objectif

Permettre un **accès distant complet (vidéo + clavier/souris)** à une machine physique, comme un serveur Proxmox, **même sans OS ou accès SSH actif**, via :
- Capture HDMI vers USB
- Affichage du flux en direct
- Contrôle clavier/souris distant
- Connexion sécurisée via VPN
- Interface web simple et restreinte

---

## 🧰 Matériel utilisé

- 🟠 Orange Pi Zero 2 (ARM64)
- 🎥 Dongle HDMI → USB (chipset MacroSilicon MS2109)
- 🖱️ Clé USB OTG pour clavier/souris ou `uinput` pour l’émulation
- 🧷 Alimentation fiable + refroidissement passif
- 🌐 Connexion Ethernet stable

---

## 🛠️ Logiciels & outils

| Composant              | Fonction                                    |
|------------------------|---------------------------------------------|
| **Armbian (Debian)**   | OS léger et stable                          |
| **MJPEG-Streamer**     | Streaming du flux vidéo (USB HDMI)          |
| **OpenVPN**            | Connexion sécurisée                         |
| **Flask**              | Interface web minimaliste                   |
| **Wake-on-LAN**        | Réveil du serveur distant                   |
| **iptables** / `ip`    | Filtrage d'accès à l'interface web          |
| **Python / Bash**      | Scripts d’automatisation                    |

---

## 📐 Schéma du système

```text
┌───────────────┐         HDMI         ┌────────────┐
│ Serveur cible │────────────────────►│ Dongle USB │
└───────────────┘                     └─────┬──────┘
                                           │ USB
                               ┌───────────▼────────────┐
                               │ Orange Pi Zero 2       │
                               │ - MJPEG-Streamer       │
                               │ - Interface Flask       │
                               │ - OpenVPN + WOL        │
                               └───────────┬────────────┘
                                           │
                                       🔐 VPN
                                           │
                                 ┌─────────▼────────┐
                                 │ PC client autorisé│
                                 └──────────────────┘
