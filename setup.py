from setuptools import setup, find_packages

setup(
    name='moosez',
    version='2.2.30',
    author='Lalith Kumar Shiyam Sundar | Sebastian Gutschmayer',
    author_email='Lalith.shiyamsundar@meduniwien.ac.at',
    description='An AI-inference engine for 3D clinical and preclinical whole-body segmentation tasks',
    python_requires='>=3.9',
    long_description='mooseZ is an AI-inference engine based on nnUNet, designed for 3D clinical and preclinical'
                     ' whole-body segmentation tasks. It serves models tailored towards different modalities such'
                     ' as PET, CT, and MR. mooseZ provides fast and accurate segmentation results, making it a '
                     'reliable tool for medical imaging applications.',
    url='https://github.com/QIMP-Team/mooseZ',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='moosez model-zoo nnUNet medical-imaging tumor-segmentation organ-segmentation bone-segmentation'
             ' lung-segmentation muscle-segmentation fat-segmentation vessel-segmentation'
             ' vertebral-segmentation rib-segmentation'
             ' preclinical-segmentation clinical-segmentation',
    packages=find_packages(),
    install_requires=[
        'nnunetv2',
        'nibabel',
        'halo',
        'pandas',
        'SimpleITK',
        'pydicom',
        'argparse',
        'imageio',
        'numpy',
        'mpire',
        'openpyxl',
        'matplotlib',
        'pyfiglet',
        'natsort',
        'pillow',
        'colorama',
        'rich',
        'pandas',
        'dicom2nifti',
        'emoji',
        'dask',
    ],
    entry_points={
        'console_scripts': [
            'moosez=moosez.moosez:main',
            'download_moosez_model=moosez.moosez_download_models:main',
        ],
    },
)
