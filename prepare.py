#!/usr/bin/env python3
import operators
import tempfile

def operate(operator_name, content):
    func = getattr(operators, operator_name, None)
    if func is None:
        return content
    else:
        return func(content)

def main():
    content = ''
    operator_name = ''
    _, fout_name = tempfile.mkstemp(prefix='arena_')
    with open(fout_name, 'w') as fout:
        with open('template.txt') as fin:
            for line in fin:
                if line.startswith('#####'):
                    print(operator_name)
                    fout.write(operate(operator_name, content))
                    fout.write(line)
                    content = ''
                    line.strip()
                    operator_name = line[5:-6]
                else:
                    content += line
            if content:
                fout.write(operate(operator_name, content))
        print(fout_name)

if __name__ == '__main__':
    main()