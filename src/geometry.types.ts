/**
 * The orthogonal axes about which flexure (i.e. bending) occurs.
 */
 export type FlexuralAxis = 'X-X' | 'Y-Y';

 /**
  * Represents a generic 2D geometry.
  */
 export interface I2Dimensional {
     /**
      * The geometric area.
      */
     area(): number;
 
     /**
      * The geometric perimeter.
      */
     perimeter(): number;
 
     /**
      * The geometric second moment of area about a given axis.
      * @param rotationAbout the axis about which the section bends.
      */
     secondMomentOfArea(rotationAbout: FlexuralAxis): number; 
 }
 
 /**
  * Represents a generic 3D geometry.
  */
 export interface I3Dimensional { 
     /**
      * The geometric volume.
      */
     volume(): number;
 }