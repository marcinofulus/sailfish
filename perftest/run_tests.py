#!/usr/bin/python -u

# Usage: perftest/run_tests.py <testsuite_name>

from examples import lbm_ldc
from examples import lbm_poiseuille
from examples import lbm_poiseuille_3d
from examples import sc_phase_separation
from examples.binary_fluid import sc_separation_2d
from examples.binary_fluid import fe_separation_2d
from examples.binary_fluid import fe_viscous_fingering

from models import single_fluid
from models import binary_fluid

from tests import run_suite

from optparse import OptionParser

model_tests = {
    'd2q9_bgk': {
        'options': {'lat_nx': 512, 'lat_ny': 512, 'model': 'bgk', 'grid': 'D2Q9'},
        'run': lambda settings: single_fluid.TestSim(single_fluid.TestGeo2D, settings),
    },

    'd2q9_mrt': {
        'options': {'lat_nx': 512, 'lat_ny': 512, 'model': 'mrt', 'grid': 'D2Q9'},
        'run': lambda settings: single_fluid.TestSim(single_fluid.TestGeo2D, settings),
    },

    'd3q13_mrt': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'mrt', 'grid': 'D3Q13'},
        'run': lambda settings: single_fluid.TestSim(single_fluid.TestGeo3D, settings),
    },

    'd3q15_bgk': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'bgk', 'grid': 'D3Q15'},
        'run': lambda settings: single_fluid.TestSim(single_fluid.TestGeo3D, settings),
    },

    'd3q15_mrt': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'mrt', 'grid': 'D3Q15'},
        'run': lambda settings: single_fluid.TestSim(single_fluid.TestGeo3D, settings),
    },

    'd3q19_bgk': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'bgk', 'grid': 'D3Q19'},
        'run': lambda settings: single_fluid.TestSim(single_fluid.TestGeo3D, settings),
    },

    'd3q19_mrt': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'mrt', 'grid': 'D3Q19'},
        'run': lambda settings: single_fluid.TestSim(single_fluid.TestGeo3D, settings),
    },

    'bin_d2q9_sc': {
        'options': {'lat_nx': 512, 'lat_ny': 512, 'model': 'bgk', 'grid': 'D2Q9'},
        'run': lambda settings: binary_fluid.SCTestSim(binary_fluid.TestGeo2D, settings),
    },

    'bin_d2q9_fe_bgk': {
        'options': {'lat_nx': 512, 'lat_ny': 512, 'model': 'bgk', 'grid': 'D2Q9'},
        'run': lambda settings: binary_fluid.FETestSim(binary_fluid.TestGeo2D, settings),
    },

    'bin_d2q9_fe_mrt': {
        'options': {'lat_nx': 512, 'lat_ny': 512, 'model': 'femrt', 'grid': 'D2Q9'},
        'run': lambda settings: binary_fluid.FETestSim(binary_fluid.TestGeo2D, settings),
    },

    'bin_d3q15_sc': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'bgk', 'grid': 'D3Q15'},
        'run': lambda settings: binary_fluid.SCTestSim(binary_fluid.TestGeo3D, settings),
    },

    'bin_d3q19_sc': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'bgk', 'grid': 'D3Q19'},
        'run': lambda settings: binary_fluid.SCTestSim(binary_fluid.TestGeo3D, settings),
    },

    'bin_d3q19_fe': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'bgk', 'grid': 'D3Q19'},
        'run': lambda settings: binary_fluid.FETestSim(binary_fluid.TestGeo3D, settings),
    },

    'bin_d3q19_fe_mrt': {
        'options': {'lat_nx': 512, 'lat_ny': 32, 'lat_nz': 32, 'model': 'femrt', 'grid': 'D3Q19'},
        'run': lambda settings: binary_fluid.FETestSim(binary_fluid.TestGeo3D, settings),
    },
}

# Tests to run.
example_tests = {
    '2d_ldc_small': {
        'options': {'lat_nx': 128, 'lat_ny': 128},
        'run': lambda settings: lbm_ldc.LDCSim(lbm_ldc.LBMGeoLDC, settings),
    },

    '2d_ldc_large': {
        'options': {'lat_nx': 1024, 'lat_ny': 1024},
        'run': lambda settings: lbm_ldc.LDCSim(lbm_ldc.LBMGeoLDC, settings),
    },

    '2d_poiseuille_small': {
        'options': {'lat_nx': 128, 'lat_ny': 128},
        'run': lambda settings: lbm_poiseuille.LPoiSim(lbm_poiseuille.LBMGeoPoiseuille, defaults=settings),
    },

    '2d_poiseuille_large': {
        'options': {'lat_nx': 1024, 'lat_ny': 1024},
        'run': lambda settings: lbm_poiseuille.LPoiSim(lbm_poiseuille.LBMGeoPoiseuille, defaults=settings),
    },

    '3d_poiseuille_d3q13': {
        'options': {'lat_nx': 128, 'lat_ny': 128, 'lat_nz': 128, 'grid': 'D3Q13'},
        'run': lambda settings: lbm_poiseuille_3d.LPoiSim(lbm_poiseuille_3d.LBMGeoPoiseuille, defaults=settings),
    },

    '3d_poiseuille_d3q15': {
        'options': {'lat_nx': 128, 'lat_ny': 128, 'lat_nz': 128, 'grid': 'D3Q15'},
        'run': lambda settings: lbm_poiseuille_3d.LPoiSim(lbm_poiseuille_3d.LBMGeoPoiseuille, defaults=settings),
    },

    '3d_poiseuille_d3q19': {
        'options': {'lat_nx': 128, 'lat_ny': 128, 'lat_nz': 128, 'grid': 'D3Q19'},
        'run': lambda settings: lbm_poiseuille_3d.LPoiSim(lbm_poiseuille_3d.LBMGeoPoiseuille, defaults=settings),
    },

    '2d_sc_phase_sep_small': {
        'options': {'lat_nx': 128, 'lat_ny': 128},
        'run': lambda settings: sc_phase_separation.SCSim(sc_phase_separation.GeoSC, defaults=settings),
    },

    '2d_sc_phase_sep_large': {
        'options': {'lat_nx': 1024, 'lat_ny': 1024},
        'run': lambda settings: sc_phase_separation.SCSim(sc_phase_separation.GeoSC, defaults=settings),
    },

    '2d_bin_sc_phase_sep_small': {
        'options': {'lat_nx': 128, 'lat_ny': 128},
        'run': lambda settings: sc_separation_2d.SCSim(sc_separation_2d.GeoSC, defaults=settings),
    },

    '2d_bin_sc_phase_sep_large': {
        'options': {'lat_nx': 1024, 'lat_ny': 1024},
        'run': lambda settings: sc_separation_2d.SCSim(sc_separation_2d.GeoSC, defaults=settings),
    },

    '2d_bin_fe_sep_small': {
        'options': {'lat_nx': 128, 'lat_ny': 128},
        'run': lambda settings: fe_separation_2d.FESim(fe_separation_2d.GeoFE, defaults=settings),
    },

    '2d_bin_fe_sep_large': {
        'options': {'lat_nx': 1024, 'lat_ny': 1024},
        'run': lambda settings: fe_separation_2d.FESim(fe_separation_2d.GeoFE, defaults=settings),
    },

    '3d_bin_fe_fingering': {
        'options': {'lat_nx': 448, 'lat_ny': 48, 'lat_nz': 38},
        'run': lambda settings: fe_viscous_fingering.FEFingerSim(fe_viscous_fingering.GeoFEFinger, defaults=settings),
    },
}


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-b', '--block_scan', dest='block_scan', help='perform a scan over block sizes', action='store_true', default=False)
    parser.add_option('-d', '--double', dest='double', help='run tests in double precision', action='store_true', default=False)
    options, args = parser.parse_args()

    suite = globals()[args[0]]

    if options.block_scan:
        run_suite(suite, args[1:], block_sizes=[32 * x for x in  range(1,9)], double=options.double)
    else:
        run_suite(suite, args[1:], double=options.double)
