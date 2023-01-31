# project 1

num_str1 = input('Input rods: ')
print("You Input "  + num_str1  +" rods")

int1 = int(num_str1)
int2 = int(40)
float1 = float(5.0292)
float2 = float(0.3048)
float3 = float(1609.34)
float4 = float(3.1)
#formulas
Meters = (int1*float1) 
Feet = ((int1*float1)/float2)
Miles = ((int1*float1)/float3)
Furlongs = (int1/int2)
Minutes = ((((int1*float1)/float3)/float4)*60)
#printing conversions
print ('Conversions')
print( "Meters:" , Meters)
print( "Feet:" , Feet)
print( "Miles:" , Miles)
print( "Furlongs:" , Furlongs)
print( "Minutes to walk" + num_str1  +" rods:" + str(Minutes))

