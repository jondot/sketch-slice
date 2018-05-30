import click
from .sketch_slice import bundle, export, IO
from .real_io import RealIO
from os.path import splitext


@click.command()
@click.argument('sketchfile', required=True)
@click.option('--prefix', default='ex-', help="Prefix for layers to filter.")
@click.option(
    '--output',
    help="Directory to output to. Defaults to same name as sketch file.")
@click.option(
    '--dryrun', type=click.BOOL, help="If set, will simulate running.")
def main(sketchfile, prefix, output, dryrun):
    """Process SKETCHFILE into the destination folder. Set SKETCHTOOL_BIN env variable to sketchtool if not found."""
    if not output:
        (output, _) = splitext(sketchfile)

    io = IO() if dryrun else RealIO()
    io.mkdir(output)

    io.headline("Processing: {}".format(sketchfile))
    io.headline("Exporting layout to: {}".format(output))
    bundle(sketchfile, output, prefix, io=io)

    io.headline("Exporting images to: {}".format(output))
    export(sketchfile, output, io=io)


if __name__ == '__main__':
    main()
