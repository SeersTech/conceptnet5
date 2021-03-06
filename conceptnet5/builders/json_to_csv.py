from __future__ import unicode_literals, print_function
from conceptnet5.formats.json_stream import read_json_stream
import codecs


def convert_to_tab_separated(input_filename, output_filename):
    out_stream = codecs.open(output_filename, 'w', encoding='utf-8')
    for info in read_json_stream(input_filename):
        if info['surfaceText'] is None:
            info['surfaceText'] = ''
        info['weight'] = str(info['weight'])
        columns = [
            'uri', 'rel', 'start', 'end', 'context', 'weight', 'source_uri',
            'id', 'dataset', 'surfaceText'
        ]
        column_values = [info.get(col) for col in columns]
        line = '\t'.join(column_values)
        print(line, file=out_stream)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='JSON-stream file of input')
    parser.add_argument('output', help='CSV file to output to')
    args = parser.parse_args()
    convert_to_tab_separated(args.input, args.output)


if __name__ == '__main__':
    main()
