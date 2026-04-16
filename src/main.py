import click
from engine import SteganoShield

@click.group()
def cli():
    pass

@cli.command()
@click.option('--img', help='Input image path')
@click.option('--msg', help='Message to hide')
@click.option('--pwd', prompt=True, hide_input=True)
def hide(img, msg, pwd):
    shield = SteganoShield(pwd)
    shield.encode(img, msg, "assets/hidden_output.png")

@cli.command()
@click.option('--img', help='Image to decode')
@click.option('--pwd', prompt=True, hide_input=True)
def reveal(img, pwd):
    shield = SteganoShield(pwd)
    print(f"Decoded: {shield.decode(img)}")

if __name__ == "__main__":
    cli()
