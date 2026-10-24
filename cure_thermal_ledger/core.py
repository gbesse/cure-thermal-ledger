import math
from .common import number,unique_ids

def run(data):
 A=number(data['prefactor_per_s'],0,1e12);E=number(data['activation_j_per_mol'],0,1e9);end=number(data['end_time_s'],0,1e9);segments=data['segments'];unique_ids(segments)
 if len(segments)>1000:raise ValueError('segments')
 parsed=[]
 for s in segments:
  a=number(s['start_s'],0,end);z=number(s['end_s'],a,end);lo=number(s['temperature_low_k'],1e-9,1e6);hi=number(s['temperature_high_k'],lo,1e6)
  if z==a:raise ValueError('zero_interval')
  parsed.append((a,z,lo,hi,s['id']))
 parsed.sort();cursor=0;low=0;high=0;gaps=[];parts=[]
 def rate(T):return A*math.exp(-E/(8.31446261815324*T))
 for a,z,lo,hi,name in parsed:
  if a<cursor:raise ValueError('overlap')
  if a>cursor:gaps.append([cursor,a]);high+=A*(a-cursor)
  dl=(z-a)*rate(lo);dh=(z-a)*rate(hi);low+=dl;high+=dh;parts.append({'id':name,'exposure_bounds':[dl,dh]});cursor=z
 if cursor<end:gaps.append([cursor,end]);high+=A*(end-cursor)
 target=number(data.get('target_conversion',.9),0,1);bounds=[-math.expm1(-low),-math.expm1(-high)];status='below_target' if bounds[1]<target else ('at_least_target' if bounds[0]>=target else 'uncertain')
 return {'conversion_bounds':bounds,'exposure_bounds':[low,high],'missing_time_ranges_s':gaps,'complete_temperature_trace':not gaps,'parts':parts,'target_relation_under_model':status,'model':'piecewise_isothermal_first_order_arrhenius_no_heat_transfer'}
