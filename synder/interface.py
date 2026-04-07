

import click
from .solsynder import Synder

# ---------------------------------------------------------           # Copyright (c) 2026 Mark. All rights reserved.                       # Unauthorized copying of this file, via any medium, is               # strictly prohibited. Written by Mark (iamnothimbutwe) on Github.
# ---------------------------------------------------------

@click.group
@click.version_option(version='Solsynder v0.3.64')
@click.pass_context
def sin(ctx):
    ctx.obj = Synder()


@sin.command()
@click.pass_obj
def pin(synder):
    synder.pin()


