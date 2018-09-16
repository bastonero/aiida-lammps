
def generate_LAMMPS_potential(data):
    #potential_file = '# Potential file generated by aiida plugin (please check citation in the orignal file)\n'

    potential_file = ''
    for line in data['file_contents']:
        potential_file += '{}'.format(line)

    return potential_file


def get_input_potential_lines(data, names=None, potential_filename='potential.pot'):

    lammps_input_text = 'pair_style      eam/{}\n'.format(data['type'])
    lammps_input_text += 'pair_coeff      * * {} {}\n'.format(potential_filename, ' '.join(names))

    return lammps_input_text

DEFAULT_UNITS = 'metal'