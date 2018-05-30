import envoy
import json
import os

SKETCH_TOOL = os.environ.get(
    'SKETCHTOOL_BIN',
    '/Applications/Sketch.app/Contents/Resources/sketchtool/bin/sketchtool')
if not os.path.exists(SKETCH_TOOL):
    print('Error: cannot find sketchtool under:\n\t' + SKETCH_TOOL)
    exit(1)


def dump(file):
    return json.loads(envoy.run(SKETCH_TOOL + ' dump {}'.format(file)).std_out)


def export(file, to="."):
    return envoy.run(
        SKETCH_TOOL + ' export slices --group-contents --output={} {}'.format(
            to, file)).std_out
