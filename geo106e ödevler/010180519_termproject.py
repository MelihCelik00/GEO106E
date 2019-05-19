# Melih Safa Çelik 010180519
import math
import numpy as np

def xyz2ell(x_519,y_519,z_519):
    """
            This function converts 3D cartesian coordinates to
            ellipsoidal coordinates using GRS80 parameters
            Parameters:
            x, y, z (type: float, unit: meters)
            Return:
            latitude, longitude (type: float, unit: degree decimal)
            ellHeight (type: float, unit: meters)
    """
    sma_519 = 6378137.0000  # semi-major
    smb_519 = 6356752.3141  # semi-minor

    longitude_rad_519 = math.atan2(y_519, x_519)
    longitude_519 = ( longitude_rad_519 * 180) / ( math.pi )
    N_519 = sma_519
    ellHeight_519 = ( ( ( x_519 ** 2 ) + ( y_519 ** 2 ) + ( z_519 ** 2 ) ) ** 0.5 ) - ( ( sma_519 * smb_519 ) ** 0.5 )
    p_519 = ( ( x_519 ** 2 ) + ( y_519 ** 2 ) ) ** 1/2
    e_519 = ( ( sma_519 ** 2 ) - ( smb_519 ** 2 ) ) / ( sma_519 ** 2 )
    latitude_rad_519 = math.atan2( ( z_519 ), ( ( 1 - ( ( e_519 * N_519 ) / ( N_519 + ellHeight_519 ) ) ) * p_519 ) )

    while True: #In this block, we are creating loop.

        delta1_519 = ( math.atan2( z_519 , ( ( 1 - ( ( e_519 * N_519 ) / ( N_519 + ellHeight_519 ) ) ) * p_519 ) ) ) - latitude_rad_519
        delta2_519 = ( sma_519 / ( ( 1 - e_519*math.sin( latitude_rad_519 ) * math.sin( latitude_rad_519 ) ) ) ** ( 1/2 ) ) - N_519
        delta3_519 = ( ( p_519 / math.cos( latitude_rad_519 ) ) - N_519 ) - ellHeight_519

        if (abs(delta1_519) < (10**-8) and abs(delta2_519) < (10**-4) and abs(delta3_519) < (10**-4)):
            break
        N_519 = sma_519 / ( ( 1 - e_519 * math.sin( latitude_rad_519 ) * math.sin( latitude_rad_519 ) ) ) ** (0.5)
        ellHeight_519 = ( p_519 / math.cos( latitude_rad_519 ) ) - N_519
        latitude_rad_519 = math.atan2( z_519, ( ( 1 - ( ( e_519 * N_519 ) / ( N_519+ellHeight_519)))*p_519))

    N_519 = sma_519 / ( ( 1 - e_519 * math.sin( latitude_rad_519 ) * math.sin( latitude_rad_519 ) ) ) ** (0.5)
    ellHeight_519 = (( p_519 / math.cos( latitude_rad_519 ) ) - N_519)
    latitude_rad_519 = math.atan2( z_519, ( ( 1 - ( ( e_519 * N_519 ) / ( N_519 + ellHeight_519 ) ) ) * p_519 ) )
    latitude_519 = ( latitude_rad_519 * 180 ) / ( math.pi )

    return latitude_519, longitude_519, ellHeight_519

def ell2xyz(latitude_519,longitude_519,ellHeight_519):
    """
            This function converts ellipsoidal coordinates to
        Cartesian coordinates using GRS80 parameters
        Parameters:
            Return:
            latitude, longitude (type: float, unit: degree decimal)
            ellHeight (type: float, unit: meters)
            x, y, z (type: float, unit: meters)
    """
    sma_519 = 6378137.0  # semi-major axis of ellipsoid
    smb_519 = 6356752.3141  # semi-minor axis of ellipsoid

    e_519 = ( ( sma_519 ** 2 ) - ( smb_519 ** 2 ) ) / ( sma_519 ** 2 )
    latitude_rad_519 = ( ( latitude_519 ) * math.pi / 180)
    longitude_rad_519 = ( ( longitude_519 ) * math.pi / 180)

    N_519 = (sma_519 / ( ( 1 - e_519 * math.sin( latitude_rad_519 ) * math.sin( latitude_rad_519 ) ) ** (0.5) ) )

    x_519 = ( N_519 + ellHeight_519 ) * math.cos( latitude_rad_519 ) * math.cos( longitude_rad_519 )
    y_519 = ( N_519 + ellHeight_519 ) * math.cos( latitude_rad_519 ) * math.sin( longitude_rad_519 )
    z_519 = ( ( ( 1 - e_519 ) * N_519 ) + ellHeight_519 ) * math.sin( latitude_rad_519 )

    return x_519,y_519,z_519

def degree2dms(decimal_519):
    """
        This function converts decimal degree to degree minute seconds
        Parameters:
        Return:
        decimal (type: float, unit: degree decimal)
        dms (type: string, format: 'DD MM SS.SSSS', example: '41 30 25.3215' )
    """
    decimal_519 = float(decimal_519)
    d_519 = int(decimal_519)
    m_519 = int(( decimal_519 - d_519 ) * 60 )
    s_519 = ( decimal_519 - d_519 - m_519 / 60 ) * (3600)
    dms_519 = "{} {} {}".format(d_519,m_519,format(s_519,".4f"))

    return dms_519