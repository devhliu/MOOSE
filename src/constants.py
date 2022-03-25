# Hard-coded variables

CROPPED_BRAIN_FROM_PET = "cropped-brain-from-PET_0000.nii.gz"
CROPPED_PADDING = 15  # in mm
CROPPED_SPINE_FROM_CT = "cropped-spine-from-ct_0000.nii.gz"
NUM_OF_ORGANS = 12
NUM_OF_BONES = 20
NUM_OF_FAT_MUSCLE = 3
NUM_OF_PSOAS = 1
NUM_OF_BRAIN = 83
DUAL_ORGANS = [
    "Adrenal-glands",
    "Kidneys",
    "Lung",
    "Carpal",
    "Clavicle",
    "Femur",
    "Fibula",
    "Humerus",
    "Metacarpal",
    "Metatarsal",
    "Patella",
    "Fingers",
    "Radius",
    "Scapula",
    "Tarsal",
    "Tibia",
    "Toes",
    "Ulna",
    "Psoas",
]

ORGAN_INDEX = {
    1: 'Adrenal-glands',
    2: 'Aorta',
    3: 'Bladder',
    4: 'Brain',
    5: 'Heart',
    6: 'Kidneys',
    7: 'Liver',
    8: 'Pancreas',
    9: 'Spleen',
    10: 'Thyroid',
    11: 'Inferior-vena-cava',
    12: 'Lung',
    13: 'Carpal',
    14: 'Clavicle',
    15: 'Femur',
    16: 'Fibula',
    17: 'Humerus',
    18: 'Metacarpal',
    19: 'Metatarsal',
    20: 'Patella',
    21: 'Pelvis',
    22: 'Phalanges-of-the-hand',
    23: 'Radius',
    24: 'Ribcage',
    25: 'Scapula',
    26: 'Skull',
    27: 'Spine',
    28: 'Sternum',
    29: 'Tarsal',
    30: 'Tibia',
    31: 'Phalanges-of-the-feet',
    32: 'Ulna',
    33: 'Skeletal-muscle',
    34: 'Subcutaneous-fat',
    35: 'Torso-fat',
    36: 'Psoas',
    37: 'R-Hippocampus',
    38: 'L-Hippocampus',
    39: 'R-Amygdala',
    40: 'L-Amygdala',
    41: 'R-Anterior-temporal-lobe-medial-part',
    42: 'L-Anterior-temporal-lobe-medial-part',
    43: 'R-Anterior-temporal-lobe-lateral-part',
    44: 'L-Anterior-temporal-lobe-lateral-part',
    45: 'R-Parahippocampal-and-ambient-gyri',
    46: 'L-Parahippocampal-and-ambient-gyri',
    47: 'R-Superior-temporal-gyrus-posterior-part',
    48: 'L-Superior-temporal-gyrus-posterior-part',
    49: 'R-Middle-and-inferior-temporal-gyrus',
    50: 'L-Middle-and-inferior-temporal-gyrus',
    51: 'R-Fusiform-gyrus',
    52: 'L-Fusiform-gyrus',
    53: 'R-Cerebellum',
    54: 'L-Cerebellum',
    55: 'Brainstem',
    56: 'L-Insula',
    57: 'R-Insula',
    58: 'L-Lateral-remainder-of-occipital-lobe',
    59: 'R-Lateral-remainder-of-occipital-lobe',
    60: 'L-Cingulate-gyrus-gyrus-cinguli-anterior-part',
    61: 'R-Cingulate-gyrus-gyrus-cinguli-anterior-part',
    62: 'L-Cingulate-gyrus-gyrus-cinguli-posterior-part',
    63: 'R-Cingulate-gyrus-gyrus-cinguli-posterior-part',
    64: 'L-Middle-frontal-gyrus',
    65: 'R-Middle-frontal-gyrus',
    66: 'L-Posterior-temporal-lobe',
    67: 'R-Posterior-temporal-lobe',
    68: 'L-Inferiolateral-remainder-of-parietal-lobe',
    69: 'R-Inferiolateral-remainder-of-parietal-lobe',
    70: 'L-Caudate-nucleus',
    71: 'R-Caudate-nucleus',
    72: 'L-Nucleus-accumbens',
    73: 'R-Nucleus-accumbens',
    74: 'L-Putamen',
    75: 'R-Putamen',
    76: 'L-Thalamus',
    77: 'R-Thalamus',
    78: 'L-Pallidum',
    79: 'R-Pallidum',
    80: 'Corpus-callosum',
    81: 'R-Lateral-ventricle-excluding-temporal-horn',
    82: 'L-Lateral-ventricle-excluding-temporal-horn',
    83: 'R-Lateral-ventricle-temporal-horn',
    84: 'L-Lateral-ventricle-temporal-horn',
    85: 'Third-ventricle',
    86: 'L-Precentral-gyrus',
    87: 'R-Precentral-gyrus',
    88: 'L-Straight-gyrus',
    89: 'R-Straight-gyrus',
    90: 'L-Anterior-orbital-gyrus',
    91: 'R-Anterior-orbital-gyrus',
    92: 'L-Inferior-frontal-gyrus',
    93: 'R-Inferior-frontal-gyrus',
    94: 'L-Superior-frontal-gyrus',
    95: 'R-Superior-frontal-gyrus',
    96: 'L-Postcentral-gyrus',
    97: 'R-Postcentral-gyrus',
    98: 'L-Superior-parietal-gyrus',
    99: 'R-Superior-parietal-gyrus',
    100: 'L-Lingual-gyrus',
    101: 'R-Lingual-gyrus',
    102: 'L-Cuneus',
    103: 'R-Cuneus',
    104: 'L-Medial-orbital-gyrus',
    105: 'R-Medial-orbital-gyrus',
    106: 'L-Lateral-orbital-gyrus',
    107: 'R-Lateral-orbital-gyrus',
    108: 'L-Posterior-orbital-gyrus',
    109: 'R-Posterior-orbital-gyrus',
    110: 'L-Substantia-nigra',
    111: 'R-Substantia-nigra',
    112: 'L-Subgenual-frontal-cortex',
    113: 'R-Subgenual-frontal-cortex',
    114: 'L-Subcallosal-area',
    115: 'R-Subcallosal-area',
    116: 'L-Pre-subgenual-frontal-cortex',
    117: 'R-Pre-subgenual-frontal-cortex',
    118: 'L-Superior-temporal-gyrus-anterior-part',
    119: 'R-Superior-temporal-gyrus-anterior-part'
}
