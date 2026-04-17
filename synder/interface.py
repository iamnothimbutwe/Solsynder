

import click
from .solsynder import Synder

# ---------------------------------------------------------           # Copyright (c) 2026 Mark. All rights reserved.                       # Unauthorized copying of this file, via any medium, is               # strictly prohibited. Written by Mark (iamnothimbutwe) on Github.
# ---------------------------------------------------------

@click.group
@click.version_option(version='Solsynder v0.4.70')
@click.pass_context
def sin(ctx):
    ctx.obj = Synder()


@sin.command()
@click.option('--cont','-c',default=None,help='giving a value to this will give the user a 3D render of the full real-time solar system positions of all major planets and dwarfs in their real [with real osculating elements] orbits ++ plus ++ the detailed Earth dashboard with ita very own 2D render real-time position in real orbit')
@click.option('--full','-f',default=None,help='giving a value to this will only show the 3D projection without the earth+2D detailed dashboard')
@click.pass_obj
def pin(synder,full,cont):
    synder.pin(full,cont)


