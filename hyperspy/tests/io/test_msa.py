import StringIO

from nose.tools import assert_true, assert_equal
import os.path

from nose.tools import assert_equal, assert_true

from hyperspy.io import load

my_path = os.path.dirname(__file__)

example1_parameters = {
    u'BEAMDIAM -nm': 100.0,
    u'BEAMKV   -kV': 120.0,
    u'CHOFFSET': -168.0,
    u'COLLANGLE-mR': 3.4,
    u'CONVANGLE-mR': 1.5,
    u'DATATYPE': u'XY',
    u'DATE': u'01-OCT-1991',
    u'DWELLTIME-ms': 100.0,
    u'ELSDET': u'SERIAL',
    u'EMISSION -uA': 5.5,
    u'FORMAT': u'EMSA/MAS Spectral Data File',
    u'MAGCAM': 100.0,
    u'NCOLUMNS': 1.0,
    u'NPOINTS': 20.0,
    u'OFFSET': 520.13,
    u'OPERMODE': u'IMAG',
    u'OWNER': u'EMSA/MAS TASK FORCE',
    u'PROBECUR -nA': 12.345,
    u'SIGNALTYPE': u'ELS',
    u'THICKNESS-nm': 50.0,
    u'TIME': u'12:00',
    u'TITLE': u'NIO EELS OK SHELL',
    u'VERSION': u'1.0',
    u'XLABEL': u'Energy',
    u'XPERCHAN': 3.1,
    u'XUNITS': u'eV',
    u'YLABEL': u'Counts',
    u'YUNITS': u'Intensity'}

example2_parameters = {
    u'ALPHA-1': u'3.1415926535',
    u'AZIMANGLE-dg': 90.0,
    u'BEAMDIAM -nm': 100.0,
    u'BEAMKV   -kV': 120.0,
    u'CHOFFSET': -20.0,
    u'COMMENT': u'The next two lines are User Defined Keywords and values',
    u'DATATYPE': u'Y',
    u'DATE': u'01-OCT-1991',
    u'EDSDET': u'SIWLS',
    u'ELEVANGLE-dg': 20.0,
    u'EMISSION -uA': 5.5,
    u'FORMAT': u'EMSA/MAS Spectral Data File',
    u'LIVETIME  -s': 100.0,
    u'MAGCAM': 100.0,
    u'NCOLUMNS': 5.0,
    u'NPOINTS': 80.0,
    u'OFFSET': 200.0,
    u'OPERMODE': u'IMAG',
    u'OWNER': u'EMSA/MAS TASK FORCE',
    u'PROBECUR -nA': 12.345,
    u'REALTIME  -s': 150.0,
    u'RESTMASS': u'511.030',
    u'SIGNALTYPE': u'EDS',
    u'SOLIDANGL-sR': u'0.13',
    u'TACTLYR  -cm': 0.3,
    u'TAUWIND  -cm': 2e-06,
    u'TBEWIND  -cm': 0.0,
    u'TDEADLYR -cm': 1e-06,
    u'THICKNESS-nm': 50.0,
    u'TIME': u'12:00',
    u'TITLE': u'NIO Windowless Spectra OK NiL',
    u'VERSION': u'1.0',
    u'XLABEL': u'X-RAY ENERGY',
    u'XPERCHAN': 10.0,
    u'XPOSITION': 123.0,
    u'XTILTSTGE-dg': 45.0,
    u'XUNITS': u'eV',
    u'YLABEL': u'X-RAY INTENSITY',
    u'YPOSITION': 456.0,
    u'YTILTSTGE-dg': 20.0,
    u'YUNITS': u'Intensity',
    u'ZPOSITION': 0.0}


class TestExample1():

    def setUp(self):
        self.s = load(os.path.join(
            my_path,
            "msa_files",
            "example1.msa"))

    def test_data(self):
        assert_equal(
            [4066.0,
             3996.0,
             3932.0,
             3923.0,
             5602.0,
             5288.0,
             7234.0,
             7809.0,
             4710.0,
             5015.0,
             4366.0,
             4524.0,
             4832.0,
             5474.0,
             5718.0,
             5034.0,
             4651.0,
             4613.0,
             4637.0,
             4429.0,
             4217.0], self.s.data.tolist())

    def test_parameters(self):
        assert_equal(
            example1_parameters,
            self.s.original_metadata.as_dictionary())


class TestExample2():

    def setUp(self):
        self.s = load(os.path.join(
            my_path,
            "msa_files",
            "example2.msa"))

    def test_data(self):
        assert_equal(
            [65.82,
             67.872,
             65.626,
             68.762,
             71.395,
             74.996,
             78.132,
             78.055,
             77.861,
             84.598,
             83.088,
             85.372,
             89.786,
             93.464,
             93.387,
             97.452,
             109.96,
             111.08,
             119.64,
             128.77,
             138.38,
             152.35,
             176.01,
             192.12,
             222.12,
             254.22,
             281.55,
             328.33,
             348.92,
             375.33,
             385.51,
             389.54,
             378.77,
             353.8,
             328.91,
             290.07,
             246.09,
             202.73,
             176.47,
             137.64,
             119.56,
             106.4,
             92.496,
             96.213,
             94.664,
             101.13,
             114.57,
             118.82,
             131.68,
             145.04,
             165.44,
             187.51,
             207.49,
             238.04,
             269.71,
             301.46,
             348.65,
             409.36,
             475.3,
             554.51,
             631.64,
             715.19,
             793.44,
             847.99,
             872.97,
             862.59,
             834.87,
             778.49,
             688.63,
             599.39,
             495.39,
             403.48,
             312.88,
             237.34,
             184.14,
             129.86,
             101.59,
             80.107,
             58.657,
             49.442], self.s.data.tolist())

    def test_parameters(self):
        assert_equal(
            example2_parameters,
            self.s.original_metadata.as_dictionary())