"""writer

"""

import math
import sys
import subprocess
import re


def main():
    with open(sys.argv[1]) as f:
        full = []
        for line in f.readlines():
            full.append([int(el) for el in line.split(' ')])
        N = len(full[0])
        M = len(full) - 2
        matrix = full[0:M]
        col_constraints = [(full[M][i], []) for i in range(0, N)]
        row_constraints = [(full[M + 1][i], []) for i in range(0, M)]

    vars_decl = []
    for row_idx, row in enumerate(matrix):
        for col_idx, el in enumerate(row):
            var_name = 'x[{0}][{1}]'.format(row_idx, col_idx)
            vars_decl.append(var_name)
            mul_val = '{0} * {1}'.format(el, var_name)
            row_constraints[row_idx][1].append(mul_val)
            col_constraints[col_idx][1].append(mul_val)

    lines = ['min: {0};'.format(' + '.join(vars_decl))]
    lines.extend(['{0} = {1};'.format(' + '.join(els), total)
                  for total, els in row_constraints])
    lines.extend(['{0} = {1};'.format(' + '.join(els), total)
                  for total, els in col_constraints])
    lines.append('bin {0};'.format(', '.join(vars_decl)))

    problem_file = sys.argv[1] + '.pl'
    with open(problem_file, 'w') as f:
        f.write('\n'.join(lines))

    out = subprocess.check_output(['lp_solve', problem_file]).decode('utf-8')
    if 'infeasible' in out:
        print(out)
    else:
        results = re.findall(r'x\[(\d+)\]\[(\d+)\]\s*(\d+)', out)
        matrix_result = [[0] * N for i in range(0, M)]
        for row, col, val in results:
            matrix_result[int(row)][int(col)] = val
        print('\n'.join([' '.join(res) for res in matrix_result]))


if __name__ == '__main__':
    main()
