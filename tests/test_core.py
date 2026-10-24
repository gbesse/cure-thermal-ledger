import unittest,math
from cure_thermal_ledger import run
class Tests(unittest.TestCase):
 def test_zero_activation_has_known_closed_form(self):
  r=run({'prefactor_per_s':2,'activation_j_per_mol':0,'end_time_s':3,'segments':[{'id':'a','start_s':0,'end_s':3,'temperature_low_k':1,'temperature_high_k':500}]});self.assertAlmostEqual(r['conversion_bounds'][0],1-math.exp(-6));self.assertEqual(r['conversion_bounds'][0],r['conversion_bounds'][1])
 def test_gap_is_unknown_not_room_temperature(self):
  r=run({'prefactor_per_s':1,'activation_j_per_mol':0,'end_time_s':3,'segments':[{'id':'a','start_s':0,'end_s':2,'temperature_low_k':300,'temperature_high_k':300}]});self.assertEqual(r['missing_time_ranges_s'],[[2,3]]);self.assertFalse(r['complete_temperature_trace']);self.assertEqual(r['exposure_bounds'],[2,3])
 def test_temperature_interval_monotonicity(self):
  r=run({'prefactor_per_s':100,'activation_j_per_mol':20000,'end_time_s':5,'segments':[{'id':'a','start_s':0,'end_s':5,'temperature_low_k':300,'temperature_high_k':400}]});self.assertLess(r['conversion_bounds'][0],r['conversion_bounds'][1])
 def test_overlapping_trace_and_nonphysical_temperature_rejected(self):
  d={'prefactor_per_s':1,'activation_j_per_mol':0,'end_time_s':3,'segments':[{'id':'a','start_s':0,'end_s':2,'temperature_low_k':300,'temperature_high_k':300},{'id':'b','start_s':1,'end_s':3,'temperature_low_k':300,'temperature_high_k':300}]}
  with self.assertRaises(ValueError):run(d)
  d['segments']=d['segments'][:1];d['segments'][0]['temperature_low_k']=0
  with self.assertRaises(ValueError):run(d)
