rvw_evalscript = """
// detection of vegetation
NDVI_RedEdge = (B08 - B05)/(B08 + B05)
threshold_vegetation = 0.45
Vegetation = NDVI_RedEdge > threshold_vegetation

// ceramic rooftop detection
RATIO_Red = B04/[B01+B02+B03+B04+B05+B06+B07]
NDBI = (B11 - B08)/(B11 + B08)
threshold_rooftop = 0.14
Rooftop = (RATIO_Red > threshold_rooftop) && (NDBI > threshold_rooftop)

// water detection
NDWI = (B03 - B08)/(B03 + B08)
threshold_water = 0.2
Water = NDWI > threshold_water

// gain to obtain smooth visualization
gain = 0.7
return [gain*Rooftop, gain*Vegetation, gain*Water]
"""

vegetation_evalscript= """
// Normalized Difference Vegetation Index
var ndvi = (B08-B04)/(B08+B04);

// Threshold for vegetation
var veg_th = 0.4;

// Simple RGB
var R = 2.5*B04;
var G = 2.5*B03;
var B = 2.5*B02;

// Transform to Black and White
var Y = 0.2*R + 0.7*G + 0.1*B;
var pixel = [Y, Y, Y];

// Change vegetation color
if(ndvi >= veg_th)
  pixel = [0.1*Y, 1.8*Y, 0.1*Y];

return pixel;
"""

barren_soil_evalscript = """
function evaluatePixel(s) {
    let val = 2.5 * ((s.B11 + s.B04)-(s.B08 + s.B02))/((s.B11 + s.B04)+(s.B08 + s.B02));
    return [2.5* val, s.B08, s.B11];
}
function setup() {
  return {
    input: [{
      bands: [
          "B02",
          "B04",
          "B08",
          "B11",
          "B12"
      ]
    }],
    output: { bands: 3 }
  }
}
"""