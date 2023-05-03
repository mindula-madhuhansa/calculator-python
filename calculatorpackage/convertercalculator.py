# length converter

# conversion factors
CONVERSION_FACTORS = {

    # from mm
    1: {
        1: 1,                               # to mm
        2: 0.1,                             # to cm
        3: 0.01,                            # to dm
        4: 0.001,                           # to m
        5: 0.000001,                        # to km
        6: 0.0393701,                       # to in
        7: 0.00328084,                      # to ft
        8: 0.00109361,                      # to yd
        9: 0.000000621371,                  # to mi
        10: 0.000000539957,                 # to NM
    },

    # from cm
    2: {
        1: 10,                              # to mm
        2: 1,                               # to cm
        3: 0.1,                             # to dm
        4: 0.01,                            # to m
        5: 0.00001,                         # to km
        6: 0.393701,                        # to in
        7: 0.0328084,                       # to ft
        8: 0.0109361,                       # to yd
        9: 0.00000621371,                   # to mi
        10: 0.00000539957,                  # to NM
    },

    # from dm
    3: {
        1: 100,                             # to mm
        2: 10,                              # to cm
        3: 1,                               # to dm
        4: 0.1,                             # to m
        5: 0.0001,                          # to km
        6: 3.93701,                         # to in
        7: 0.328084,                        # to ft
        8: 0.109361,                        # to yd
        9: 0.0000621371,                    # to mi
        10: 0.0000539957,                   # to NM
    },

    # from m
    4: {
        1: 1000,                            # to mm
        2: 100,                             # to cm
        3: 10,                              # to dm
        4: 1,                               # to m
        5: 0.001,                           # to km
        6: 39.3701,                         # to in
        7: 3.28084,                         # to ft
        8: 1.09361,                         # to yd
        9: 0.000621371,                     # to mi
        10: 0.000539957,                    # to NM
    },

    # from km
    5: {
        1: 1000000,                         # to mm
        2: 100000,                          # to cm
        3: 10000,                           # to dm
        4: 1000,                            # to m
        5: 1,                               # to km
        6: 39370.1,                         # to in
        7: 3280.84,                         # to ft
        8: 1093.61,                         # to yd
        9: 0.621371,                        # to mi
        10: 0.539957,                       # to NM
    },

    # from in
    6: {
        1: 25.4,                            # to mm
        2: 2.54,                            # to cm
        3: 0.254,                           # to dm
        4: 0.0254,                          # to m
        5: 0.0000254,                       # to km
        6: 1,                               # to in
        7: 0.0833,                          # to ft
        8: 0.0278,                          # to yd
        9: 0.0000158,                       # to mi
        10: 0.0000137,                      # to NM
    },

    # from ft
    7: {
        1: 304.8,                           # to mm
        2: 30.48,                           # to cm
        3: 3.048,                           # to dm
        4: 0.3048,                          # to m
        5: 0.0003048,                       # to km
        6: 12,                              # to in
        7: 1,                               # to ft
        8: 0.3333,                          # to yd
        9: 0.0001894,                       # to mi
        10: 0.0001646,                      # to NM
    },

    # from yd
    8: {
        1: 914.4,                           # to mm
        2: 91.44,                           # to cm
        3: 9.144,                           # to dm
        4: 0.9144,                          # to m
        5: 0.0009144,                       # to km
        6: 36,                              # to in
        7: 3,                               # to ft
        8: 1,                               # to yd
        9: 0.0005682,                       # to mi
        10: 0.0004937,                      # to NM
    },

    # from mi
    9: {
        1: 1609344,                         # to mm
        2: 160934.4,                        # to cm
        3: 16093.44,                        # to dm
        4: 1609.344,                        # to m
        5: 1.609344,                        # to km
        6: 63360,                           # to in
        7: 5280,                            # to ft
        8: 1760,                            # to yd
        9: 1,                               # to mi
        10: 0.8684,                         # to NM
    },

    # from NM
    10: {
        1: 1852000,                         # to mm
        2: 185200,                          # to cm
        3: 18520,                           # to dm
        4: 1852,                            # to m
        5: 1.852,                           # to km
        6: 72913.4,                         # to in
        7: 6076.12,                         # to ft
        8: 2025.3,                          # to yd
        9: 1.1508,                          # to mi
        10: 1,                              # to NM
    },
}


def length_converter(converter_unit, converted_unit, converter_value):
    return converter_value * CONVERSION_FACTORS[int(converter_unit)][int(converted_unit)]

