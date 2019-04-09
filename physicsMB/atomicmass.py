import periodictable as pt
from periodictable import formulas
import astropy.units as u


def atomicmass(species):
    '''
    Returns the atomic mass of an atom or molecule.

    This is really just a wrapper for
    `periodictable <https://periodictable.readthedocs.io/en/latest/index.html>`_
    but returns the mass as an astropy quantity.
    '''

    el = [e.symbol for e in pt.elements]
    if species in el:
        atom = eval('pt.'+species)
        mass = atom.mass * u.u
    else:
        try:
            mass = formulas.formula(species).mass * u.u
        except:
            print(f'Species={species} not found')
            mass = None

    return mass
