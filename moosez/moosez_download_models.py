#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------------------------------------------
# Author: Lalith Kumar Shiyam Sundar
# Institution: Medical University of Vienna
# Research Group: Quantitative Imaging and Medical Physics (QIMP) Team
# Date: 09.02.2023
# Version: 2.0.0
#
# Description:
# The main module of the mooseZ. It contains the main function that is executed when the mooseZ is run.
#
# Usage:
# The main function in this module is executed when the mooseZ is run.
#
# ----------------------------------------------------------------------------------------------------------------------

import logging
import emoji
from datetime import datetime

import colorama

from moosez import constants
from moosez import display
from moosez import download
from moosez import file_utilities
from moosez import resources
from moosez.resources import MODELS, AVAILABLE_MODELS

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO,
                    filename=datetime.now().strftime('moosez-v.2.2.31.%H-%M-%d-%m-%Y.log'),
                    filemode='w')


def main():

    colorama.init()
    display.logo()
    display.citation()

    logging.info('----------------------------------------------------------------------------------------------------')
    logging.info('                                     STARTING MOOSE-Z V.2.2.31                                       ')
    logging.info('----------------------------------------------------------------------------------------------------')

    for model_name in AVAILABLE_MODELS:

        # ----------------------------------
        # INPUT VALIDATION AND PREPARATION
        # ----------------------------------

        logging.info(' ')
        logging.info('- Model name: ' + model_name)
        logging.info(' ')
        print(' ')
        print(f'{constants.ANSI_VIOLET} {emoji.emojize(":memo:")} NOTE:{constants.ANSI_RESET}')
        print(' ')
        modalities = display.expectations(model_name)
        accelerator = resources.check_cuda()

        # ----------------------------------
        # DOWNLOADING THE MODEL
        # ----------------------------------

        print('')
        print(f'{constants.ANSI_VIOLET} {emoji.emojize(":globe_with_meridians:")} MODEL DOWNLOAD:{constants.ANSI_RESET}')
        print('')
        model_path = constants.NNUNET_RESULTS_FOLDER
        file_utilities.create_directory(model_path)
        download.model(model_name, model_path)


if __name__ == '__main__':
    main()