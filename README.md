# Solsynder

**Real-time Solar System Calendar**  
Powered by **astlo** — built entirely on mobile.

One command. One screen. Live view of the entire solar system.

---

## Features

- **Single-screen real-time dashboard** — everything refreshes in one view
- **16 solar system bodies** tracked simultaneously (planets + dwarf planets)
- **Only one dependency**: [astlo](https://github.com/iamnothimbutwe/astlopublic) (the core orbital mechanics engine)
- Dedicated **Earth State** section with rich vector information
- Real-time **orbital plot** showing Earth’s position in its orbit
- Clean terminal output with proper units:
  - Distances in **AU** and **km**
  - Velocities and other values in appropriate SI units
  - Time-related values in **minutes** where needed
  - one Osculating element ¦inclination¦ in degrees° ¦reference frame is J2000 and the epoch is real time
- Runs smoothly on mobile (Termux on Android / Itel RS4 and similar devices)
- Pure Python, lightweight, and built from scratch on a budget phone

---

>..join us at r/kenyaspacenerds..


## Quick Start

```bash
# Install (after installing astlo)
pip install -e .

# Run the calendar
solsynder pin

or just solsynder pin --help to get the help on the pin commamd


Live positions and states for Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Ceres, and other dwarf planets
Special Earth Section showing:
Current distance from Sun (AU + km)
Velocity vectors
Orbital anomalies and energy
Real-time position in the orbital plot
Clean terminal plot showing the current orbital configuration
Everything updates continuously so you can watch the solar system move in real time.

Why Solsynder?
I built this because I wanted a simple, fast way to see where everything is right now — without heavy libraries or internet.
astlo handles all the hard orbital math (osculating elements, vectors, ephemeris).
Solsynder focuses on presenting it beautifully in one screen.

It’s designed for:
Curious stargazers in Kenya
Students learning orbital mechanics
Anyone who wants to play with real solar system    data on their phone


Built on Mobile

Every line of code was written and tested on an Android phone (Itel RS4) using Termux.
No big computers.

No heavy dependencies.

Just pure Python and persistence.


Coming Soon..

Better plot customization
Export options
Search for specific bodies
More user-friendly features (open to suggestions!)

Dependencies..
astlo >= 5.71.73 (only dependency)

License..
MIT License — feel free to use, modify, and contribute.

Get Involved
Found a bug? Want a new feature?
Open an issue or pull request on GitHub.
Let’s grow Kenya Sovereign Tech together.

Made with ❤️ in Naivasha, Kenya
by Mark Macharia (iamnothimbutwe)
