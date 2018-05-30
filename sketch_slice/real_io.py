from . import sketchtool
from os import makedirs
from .sketch_slice import IO
from click import secho


class RealIO(IO):
    def headline(self, str):
        secho(str, fg='green', bold=True)

    def report(self, str):
        secho("\t" + "\n\t".join(str.splitlines()), fg='white')

    def write_file(self, to, content):
        with open(to, 'w') as f:
            f.write(content)

    def mkdir(self, to):
        try:
            makedirs(to)
        except OSError as exc:
            pass

    def export_images(self, file, to):
        return sketchtool.export(file, to)

    def get_data(self, file):
        return sketchtool.dump(file)
