import numpy as np
import nose.tools

import hyperspy.hspy as hs


class TestEELSModel:

    def setUp(self):
        s = hs.signals.EELSSpectrum(np.empty(200))
        s.set_microscope_parameters(100, 10, 10)
        s.axes_manager[-1].offset = 150
        s.add_elements(("B", "C"))
        self.m = hs.create_model(s)

    def test_suspend_auto_fsw(self):
        m = self.m
        m["B_K"].fine_structure_width = 140.
        m.suspend_auto_fine_structure_width()
        m.enable_fine_structure()
        m.resolve_fine_structure()
        nose.tools.assert_equal(140, m["B_K"].fine_structure_width)

    def test_resume_fsw(self):
        m = self.m
        m["B_K"].fine_structure_width = 140.
        m.suspend_auto_fine_structure_width()
        m.resume_auto_fine_structure_width()
        window = (m["C_K"].onset_energy.value -
                  m["B_K"].onset_energy.value -
                  hs.preferences.EELS.preedge_safe_window_width)
        m.enable_fine_structure()
        m.resolve_fine_structure()
        nose.tools.assert_equal(window, m["B_K"].fine_structure_width)

    def test_get_first_ionization_edge_energy_C_B(self):
        nose.tools.assert_equal(self.m._get_first_ionization_edge_energy(),
                                self.m["B_K"].onset_energy.value)

    def test_get_first_ionization_edge_energy_C(self):
        self.m["B_K"].active = False
        nose.tools.assert_equal(self.m._get_first_ionization_edge_energy(),
                                self.m["C_K"].onset_energy.value)

    def test_get_first_ionization_edge_energy_None(self):
        self.m["B_K"].active = False
        self.m["C_K"].active = False
        nose.tools.assert_is_none(self.m._get_first_ionization_edge_energy())

    def test_two_area_powerlaw_estimation_BC(self):
        self.m.spectrum.data = 2. * self.m.axis.axis ** (-3)  # A= 2, r=3
        self.m.spectrum.metadata.Signal.binned = False
        self.m.two_area_background_estimation()
        nose.tools.assert_almost_equal(self.m._background_components[0].A.value,
                                       2.1451237089380295)
        nose.tools.assert_almost_equal(self.m._background_components[0].r.value,
                                       3.0118980767392736)

    def test_two_area_powerlaw_estimation_C(self):
        self.m["B_K"].active = False
        self.m.spectrum.data = 2. * self.m.axis.axis ** (-3)  # A= 2, r=3
        self.m.spectrum.metadata.Signal.binned = False
        self.m.two_area_background_estimation()
        nose.tools.assert_almost_equal(self.m._background_components[0].A.value,
                                       2.3978438900878087)
        nose.tools.assert_almost_equal(self.m._background_components[0].r.value,
                                       3.031884021065014)

    def test_two_area_powerlaw_estimation_no_edge(self):
        self.m["B_K"].active = False
        self.m["C_K"].active = False
        self.m.spectrum.data = 2. * self.m.axis.axis ** (-3)  # A= 2, r=3
        self.m.spectrum.metadata.Signal.binned = False
        self.m.two_area_background_estimation()
        nose.tools.assert_almost_equal(self.m._background_components[0].A.value,
                                       2.6598803469440986)
        nose.tools.assert_almost_equal(self.m._background_components[0].r.value,
                                       3.0494030409062058)
